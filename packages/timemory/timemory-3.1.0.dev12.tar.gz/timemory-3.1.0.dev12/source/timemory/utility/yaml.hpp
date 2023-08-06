// MIT License
//
// Copyright (c) 2020, The Regents of the University of California,
// through Lawrence Berkeley National Laboratory (subject to receipt of any
// required approvals from the U.S. Dept. of Energy).  All rights reserved.
//
// Permission is hereby granted, free of charge, to any person obtaining a copy
// of this software and associated documentation files (the "Software"), to deal
// in the Software without restriction, including without limitation the rights
// to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
// copies of the Software, and to permit persons to whom the Software is
// furnished to do so, subject to the following conditions:
//
// The above copyright notice and this permission notice shall be included in all
// copies or substantial portions of the Software.
//
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
// IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
// FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
// AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
// LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
// OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
// SOFTWARE.
//

#pragma once

#include "cereal/cereal.hpp"
#include "cereal/details/util.hpp"

#include "timemory/utility/macros.hpp"
#include "timemory/utility/utility.hpp"

namespace cereal
{
//! An exception thrown when yaml fails an internal assertion
/*! @ingroup Utility */
struct YamlException : Exception
{
    YamlException(const char* what_)
    : Exception(what_)
    {}
};
}  // namespace cereal

// Inform yaml that assert will throw
#ifndef CEREAL_YAML_ASSERT_THROWS
#    define CEREAL_YAML_ASSERT_THROWS
#endif  // CEREAL_YAML_ASSERT_THROWS

// Override yaml assertions to throw exceptions by default
#ifndef CEREAL_YAML_ASSERT
#    define CEREAL_YAML_ASSERT(x)                                                        \
        if(!(x))                                                                         \
        {                                                                                \
            throw ::cereal::YamlException("yaml internal assertion failure: " #x);       \
        }
#endif  // YAML_ASSERT

// Enable support for parsing of nan, inf, -inf
#ifndef CEREAL_YAML_WRITE_DEFAULT_FLAGS
#    define CEREAL_YAML_WRITE_DEFAULT_FLAGS kWriteNanAndInfFlag
#endif

// Enable support for parsing of nan, inf, -inf
#ifndef CEREAL_YAML_PARSE_DEFAULT_FLAGS
#    define CEREAL_YAML_PARSE_DEFAULT_FLAGS kParseFullPrecisionFlag | kParseNanAndInfFlag
#endif

#include "cereal/external/base64.hpp"

#include <cstdint>
#include <istream>
#include <limits>
#include <ostream>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

namespace cereal
{
//
//======================================================================================//
//
struct YamlEntry
{
    static const int64_t npos = std::string::npos;

    bool                   prologue_is_seq    = false;
    bool                   prologue_is_map    = false;
    bool                   epilogue_is_scalar = false;
    int64_t                indent_length      = 0;
    YamlEntry*             parent             = nullptr;
    std::vector<YamlEntry> children;

    bool check_prologue(std::string line)
    {
        if(prologue_is_seq)
        {
            CEREAL_YAML_ASSERT(line.at(indent_length) != '-' &&
                               line.at(indent_length + 1) != ' ')
        }
        else if(prologue_is_map)
        {
            CEREAL_YAML_ASSERT(line.find_first_of(':') != npos)
            CEREAL_YAML_ASSERT(line.length() <= (line.find_first_of(':') + 1) ||
                               (line.length() > (line.find_first_of(':') + 1) &&
                                (line.at(line.find_first_of(':') + 1) == ' ' ||
                                 line.at(line.find_first_of(':') + 1) == '\n' ||
                                 line.at(line.find_first_of(':') + 1) == '\r')))
        }
        return true;
    }

    template <typename Tp>
    bool read(std::istream& is, Tp& val)
    {
        std::string line;
        std::getline(is, line);
        indent_length = line.find_first_not_of("\t \n\r");
        CEREAL_YAML_ASSERT(indent_length != npos)
        int64_t didx = line.find_first_of('-');
        int64_t cidx = line.find_first_of(':');
        if(didx != npos)
            prologue_is_seq = true;

        if(didx != npos && line.at(indent_length + 1) == '-')
            prologue_is_seq = true;
        if(cidx != npos)
            prologue_is_map = true;

        if(didx == npos)
            didx = -1;
        if(cidx == npos)
            cidx = -1;

        auto midx = std::max(didx, cidx);

        if(midx < line.length())
        {
            epilogue_is_scalar = true;
            auto field         = line.substr(midx + 1);
            field              = field.substr(field.find_first_not_of(" \t\n\r"));
            if(field.length() == 0)
                return false;
            int64_t bquote = field.find_first_of('"');
            int64_t equote = field.find_last_of('"');
            if(bquote < equote && bquote != npos && equote != npos)
                field = field.substr(bquote + 1, (equote - bquote - 1));
            std::istringstream iss(field);
            iss >> val;
            return true;
        }

        return false;
    }

    template <typename Tp, std::enable_if_t<(std::is_pointer<Tp>::value), int> = 0>
    static bool check_if_nullptr(Tp v)
    {
        return (v == nullptr);
    }

    template <typename Tp, std::enable_if_t<!(std::is_pointer<Tp>::value), int> = 0>
    static bool check_if_nullptr(Tp v)
    {
        return false;
    }

    template <typename Tp>
    bool write(std::ostream& os, std::ios::fmtflags flags, Tp val, std::string key = "")
    {
        PRINT_HERE("key = %s, type = %s", key.c_str(), tim::demangle<Tp>().c_str());

        using type = std::decay_t<Tp>;
        static constexpr bool is_string =
            std::is_same<type, std::string>::value || std::is_same<type, char*>::value;
        const bool is_key = (key == "KEY");

        std::stringstream ss;
        ss.setf(flags);
        std::string wrap    = "";
        std::string leading = "";
        std::string tailing = "";

        if(is_string && !is_key)
            wrap = "\"";

        if(prologue_is_seq)
            leading = "- ";

        if(prologue_is_map)
            tailing = ": ";

        ss << std::setw(indent_length) << "" << leading;

        if(!is_key)
            ss << " " << wrap << val << wrap << tailing;
        else if(is_key)
            ss << wrap << val << wrap;

        if(key.length() == 0)
            ss << tailing;

        PRINT_HERE("output = %s", ss.str().c_str());
        os << ss.str() << '\n';
        return true;
    }
};
//
//======================================================================================//
//
struct YamlWriter
{
    static const int64_t npos = std::string::npos;

    std::ostream*          os           = nullptr;
    std::ios::fmtflags     flags        = {};
    bool                   is_array     = false;
    bool                   is_object    = false;
    int64_t                indent       = 0;
    int64_t                incr         = 2;
    int64_t                array_depth  = 0;
    int64_t                object_depth = 0;
    std::vector<YamlEntry> children;
    YamlEntry*             current = nullptr;

    YamlWriter(std::ostream* _os, std::ios::fmtflags _flags = {}, int64_t _incr = 2)
    : os(_os)
    , flags(_flags)
    , incr(_incr)
    {
        children.resize(1, YamlEntry{});
        current = &children.front();
    }

    void StartArray()
    {
        PRINT_HERE("%s", "");
        is_array                 = true;
        current->prologue_is_map = true;
        indent += incr;
        array_depth += 1;
    }

    void EndArray()
    {
        PRINT_HERE("%s", "");
        indent -= incr;
        array_depth -= 1;
    }

    void StartObject()
    {
        PRINT_HERE("%s", "");
        is_object                = true;
        current->prologue_is_seq = true;
        indent += incr;
        object_depth += 1;
    }

    void EndObject()
    {
        PRINT_HERE("%s", "");
        indent -= incr;
        object_depth -= 1;
    }

    template <typename Tp>
    void save(const std::string& key)
    {
        PRINT_HERE("%s", key.c_str());
        YamlEntry _entry{};
        _entry.prologue_is_map    = current->prologue_is_map;
        _entry.prologue_is_seq    = current->prologue_is_seq;
        _entry.epilogue_is_scalar = false;
        if(is_array || is_object)
            _entry.parent = current;
        else
            _entry.parent = current->parent;
        if(os)
        {
            if(is_array || is_object)
                _entry.write(*os, flags, key, "KEY");
            else
            {
                _entry.write(*os, flags, key);
                *os << '\n';
            }
        }
        is_array  = false;
        is_object = false;
        // if(_children)
        //    _children->push_back(_entry);
    }

    template <typename Tp>
    void save(const Tp& val)
    {
        YamlEntry _entry{};
        _entry.parent             = current;
        _entry.prologue_is_map    = current->prologue_is_map;
        _entry.prologue_is_seq    = current->prologue_is_seq;
        _entry.epilogue_is_scalar = false;
        if(is_array || is_object)
            _entry.parent = current;
        else
            _entry.parent = current->parent;
        if(os)
        {
            if(is_array || is_object)
                _entry.write(*os, flags, val, "KEY");
            else
            {
                _entry.write(*os, flags, val);
                *os << '\n';
            }
        }
        is_array  = false;
        is_object = false;
        // if(_children)
        //    _children->push_back(_entry);
    }

    void* null_val = nullptr;
};

//======================================================================================//
//! An output archive designed to save data to YAML
/*! This archive uses Yaml to build serialize data to YAML.

    YAML archives provides a human readable output but at decreased
    performance (both in time and space) compared to binary archives.

    YAML archives are only guaranteed to finish flushing their contents
    upon destruction and should thus be used in an RAII fashion.

    YAML benefits greatly from name-value pairs, which if present, will
    name the nodes in the output.  If these are not present, each level
    of the output will be given an automatically generated delimited name.

    The precision of the output archive controls the number of decimals output
    for floating point numbers and should be sufficiently large (i.e. at least 20)
    if there is a desire to have binary equality between the numbers output and
    those read in.  In general you should expect a loss of precision when going
    from floating point to text and back.

    YAML archives do not output the size information for any dynamically sized
   structure and instead infer it from the number of children for a node.  This means
   that data can be hand edited for dynamic sized structures and will still be
   readable.  This is accomplished through the cereal::SizeTag object, which will
   cause the archive to output the data as a YAML array (e.g. marked by [] instead of
   {}), which indicates that the container is variable sized and may be edited.

    \ingroup Archives
*/

class YamlOutputArchive
: public OutputArchive<YamlOutputArchive>
, public traits::TextArchive
{
    enum class NodeType
    {
        StartObject,
        InObject,
        StartArray,
        InArray
    };

public:
    /*! @name Common Functionality
        Common use cases for directly interacting with an YamlOutputArchive */
    //! @{

    //! A class containing various advanced options for the YAML archive
    class Options
    {
    public:
        static const int kDefaultMaxDecimalPlaces = 324;

        //! Default options
        static Options Default() { return Options(); }

        //! Default options with no indentation
        static Options NoIndent()
        {
            return Options(kDefaultMaxDecimalPlaces, IndentChar::space, 0);
        }

        //! The character to use for indenting
        enum class IndentChar : char
        {
            space           = ' ',
            tab             = '\t',
            newline         = '\n',
            carriage_return = '\r'
        };

        //! Specify specific options for the YamlOutputArchive
        /*!
         * @param precision The precision used for floating point numbers
         * @param indentChar The type of character to indent with
         * @param indentLength The number of indentChar to use for indentation
         * @param format flags
         */
        explicit Options(int                precision    = kDefaultMaxDecimalPlaces,
                         IndentChar         indentChar   = IndentChar::space,
                         unsigned int       indentLength = 4,
                         std::ios::fmtflags fmt = std::ios::scientific | std::ios::dec |
                                                  std::ios::showpoint)
        : itsPrecision(precision)
        , itsIndentChar(static_cast<char>(indentChar))
        , itsIndentLength(indentLength)
        , itsFlags(fmt)
        {}

    private:
        friend class YamlOutputArchive;
        int                itsPrecision;
        char               itsIndentChar;
        unsigned int       itsIndentLength;
        std::ios::fmtflags itsFlags;
    };

    YamlOutputArchive(std::ostream& stream, Options const& options = Options::Default())
    : OutputArchive<YamlOutputArchive>(this)
    , itsWriter(&stream, options.itsFlags, options.itsIndentLength)
    , itsNextName(nullptr)
    {
        itsNameCounter.push(0);
        itsNodeStack.push(NodeType::StartObject);
    }

    //! Destructor, flushes the YAML
    ~YamlOutputArchive() CEREAL_NOEXCEPT
    {
        if(itsNodeStack.top() == NodeType::InObject)
            itsWriter.EndObject();
        else if(itsNodeStack.top() == NodeType::InArray)
            itsWriter.EndArray();
    }

    void saveBinaryValue(const void* data, size_t size, const char* name = nullptr)
    {
        setNextName(name);
        writeName();

        auto base64string =
            base64::encode(reinterpret_cast<const unsigned char*>(data), size);
        saveValue(base64string);
    }

    void startNode()
    {
        writeName();
        itsNodeStack.push(NodeType::StartObject);
        itsNameCounter.push(0);
    }

    void finishNode()
    {
        // if we ended up serializing an empty object or array, writeName
        // will never have been called - so start and then immediately end
        // the object/array.
        //
        // We'll also end any object/arrays we happen to be in
        switch(itsNodeStack.top())
        {
            case NodeType::StartArray:
                itsWriter.StartArray();
                // fall through
            case NodeType::InArray: itsWriter.EndArray(); break;
            case NodeType::StartObject:
                itsWriter.StartObject();
                // fall through
            case NodeType::InObject: itsWriter.EndObject(); break;
        }

        itsNodeStack.pop();
        itsNameCounter.pop();
    }

    //! Sets the name for the next node created with startNode
    void setNextName(const char* name) { itsNextName = name; }

    void saveValue(bool b) { itsWriter.save(b); }
    void saveValue(int i) { itsWriter.save(i); }
    void saveValue(unsigned u) { itsWriter.save(u); }
    void saveValue(int64_t i64) { itsWriter.save(i64); }
    void saveValue(uint64_t u64) { itsWriter.save(u64); }
    void saveValue(double d) { itsWriter.save(d); }
    void saveValue(std::string const& s) { itsWriter.save(s); }
    void saveValue(char const* s) { itsWriter.save(std::string(s)); }
    void saveValue(std::nullptr_t)
    { /*itsWriter.Null();*/
    }

private:
    // Some compilers/OS have difficulty disambiguating the above for various flavors of
    // longs, so we provide special overloads to handle these cases.

    template <class T, traits::EnableIf<sizeof(T) == sizeof(std::int32_t),
                                        std::is_signed<T>::value> = traits::sfinae>
    inline void saveLong(T l)
    {
        saveValue(static_cast<int32_t>(l));
    }

    template <class T, traits::EnableIf<sizeof(T) != sizeof(std::int32_t),
                                        std::is_signed<T>::value> = traits::sfinae>
    inline void saveLong(T l)
    {
        saveValue(static_cast<int64_t>(l));
    }

    template <class T, traits::EnableIf<sizeof(T) == sizeof(std::int32_t),
                                        std::is_unsigned<T>::value> = traits::sfinae>
    inline void saveLong(T lu)
    {
        saveValue(static_cast<uint32_t>(lu));
    }

    template <class T, traits::EnableIf<sizeof(T) != sizeof(std::int32_t),
                                        std::is_unsigned<T>::value> = traits::sfinae>
    inline void saveLong(T lu)
    {
        saveValue(static_cast<uint64_t>(lu));
    }

public:
#ifdef _MSC_VER
    //! MSVC only long overload to current node
    void saveValue(unsigned long lu) { saveLong(lu); };
#else   // _MSC_VER
        //! Serialize a long if it would not be caught otherwise
    template <class T,
              traits::EnableIf<std::is_same<T, long>::value,
                               !std::is_same<T, std::int32_t>::value,
                               !std::is_same<T, std::int64_t>::value> = traits::sfinae>
    inline void saveValue(T t)
    {
        saveLong(t);
    }

    //! Serialize an unsigned long if it would not be caught otherwise
    template <class T,
              traits::EnableIf<std::is_same<T, unsigned long>::value,
                               !std::is_same<T, std::uint32_t>::value,
                               !std::is_same<T, std::uint64_t>::value> = traits::sfinae>
    inline void saveValue(T t)
    {
        saveLong(t);
    }
#endif  // _MSC_VER

    //! Save exotic arithmetic as strings to current node
    /*! Handles long long (if distinct from other types), unsigned long (if distinct), and
     * long double */
    template <
        class T,
        traits::EnableIf<
            std::is_arithmetic<T>::value, !std::is_same<T, long>::value,
            !std::is_same<T, unsigned long>::value, !std::is_same<T, std::int64_t>::value,
            !std::is_same<T, std::uint64_t>::value,
            (sizeof(T) >= sizeof(long double) || sizeof(T) >= sizeof(long long))> =
            traits::sfinae>
    inline void saveValue(T const& t)
    {
        std::stringstream ss;
        ss.precision(std::numeric_limits<long double>::max_digits10);
        ss << t;
        saveValue(ss.str());
    }

    void writeName()
    {
        NodeType const& nodeType = itsNodeStack.top();

        // Start up either an object or an array, depending on state
        if(nodeType == NodeType::StartArray)
        {
            itsWriter.StartArray();
            itsNodeStack.top() = NodeType::InArray;
        }
        else if(nodeType == NodeType::StartObject)
        {
            itsNodeStack.top() = NodeType::InObject;
            itsWriter.StartObject();
        }

        // Array types do not output names
        if(nodeType == NodeType::InArray)
            return;

        if(itsNextName == nullptr)
        {
            std::string name = "value" + std::to_string(itsNameCounter.top()++) + "\0";
            saveValue(name);
        }
        else
        {
            saveValue(itsNextName);
            itsNextName = nullptr;
        }
    }

    //! Designates that the current node should be output as an array, not an object
    void makeArray() { itsNodeStack.top() = NodeType::StartArray; }

    //! @}

private:
    YamlWriter           itsWriter;       //!< Rapidyaml writer
    char const*          itsNextName;     //!< The next name
    std::stack<uint32_t> itsNameCounter;  //!< Counter for creating unique names
    std::stack<NodeType> itsNodeStack;
};  // YamlOutputArchive

//======================================================================================//
//! An input archive designed to load data from YAML
/*! This archive uses Yaml to read in a YAML archive.

    As with the output YAML archive, the preferred way to use this archive is in
    an RAII fashion, ensuring its destruction after all data has been read.

    Input YAML should have been produced by the YamlOutputArchive.  Data can
    only be added to dynamically sized containers (marked by YAML arrays) -
    the input archive will determine their size by looking at the number of child
   nodes. Only YAML originating from a YamlOutputArchive is officially supported,
   but data from other sources may work if properly formatted.

    The YamlInputArchive does not require that nodes are loaded in the same
    order they were saved by YamlOutputArchive.  Using name value pairs (NVPs),
    it is possible to load in an out of order fashion or otherwise skip/select
    specific nodes to load.

    The default behavior of the input archive is to read sequentially starting
    with the first node and exploring its children.  When a given NVP does
    not match the read in name for a node, the archive will search for that
    node at the current level and load it if it exists.  After loading an out of
    order node, the archive will then proceed back to loading sequentially from
    its new position.

    Consider this simple example where loading of some data is skipped:

    @code{cpp}
    // imagine the input file has someData(1-9) saved in order at the top level node
    ar( someData1, someData2, someData3 );        // XML loads in the order it sees in
   the file ar( cereal::make_nvp( "hello", someData6 ) ); // NVP given does not
                                                  // match expected NVP name, so we
   search
                                                  // for the given NVP and load that
   value ar( someData7, someData8, someData9 );        // with no NVP given, loading
   resumes at its
                                                  // current location, proceeding
   sequentially
    @endcode

    \ingroup Archives */
/*
class YamlInputArchive
: public InputArchive<YamlInputArchive>
, public traits::TextArchive
{
private:
    using ReadStream = CEREAL_YAML_NAMESPACE::IStreamWrapper;
    typedef CEREAL_YAML_NAMESPACE::GenericValue<CEREAL_YAML_NAMESPACE::UTF8<>> YAMLValue;
    typedef YAMLValue::ConstMemberIterator                MemberIterator;
    typedef YAMLValue::ConstValueIterator                 ValueIterator;
    typedef CEREAL_YAML_NAMESPACE::Document::GenericValue GenericValue;

public:
    YamlInputArchive(std::istream& stream)
    : InputArchive<YamlInputArchive>(this)
    , itsNextName(nullptr)
    , itsReadStream(stream)
    {
        itsDocument.ParseStream<>(itsReadStream);
        if(itsDocument.IsArray())
            itsIteratorStack.emplace_back(itsDocument.Begin(), itsDocument.End());
        else
            itsIteratorStack.emplace_back(itsDocument.MemberBegin(),
                                          itsDocument.MemberEnd());
    }

    ~YamlInputArchive() CEREAL_NOEXCEPT = default;

    void loadBinaryValue(void* data, size_t size, const char* name = nullptr)
    {
        itsNextName = name;

        std::string encoded;
        loadValue(encoded);
        auto decoded = base64::decode(encoded);

        if(size != decoded.size())
            throw Exception("Decoded binary data size does not match specified size");

        std::memcpy(data, decoded.data(), decoded.size());
        itsNextName = nullptr;
    };

private:
    class Iterator
    {
    public:
        Iterator()
        : itsIndex(0)
        , itsType(Null_)
        {}

        Iterator(MemberIterator begin, MemberIterator end)
        : itsMemberItBegin(begin)
        , itsMemberItEnd(end)
        , itsIndex(0)
        , itsType(Member)
        {
            if(std::distance(begin, end) == 0)
                itsType = Null_;
        }

        Iterator(ValueIterator begin, ValueIterator end)
        : itsValueItBegin(begin)
        , itsIndex(0)
        , itsType(Value)
        {
            if(std::distance(begin, end) == 0)
                itsType = Null_;
        }

        //! Advance to the next node
        Iterator& operator++()
        {
            ++itsIndex;
            return *this;
        }

        //! Get the value of the current node
        GenericValue const& value()
        {
            switch(itsType)
            {
                case Value: return itsValueItBegin[itsIndex];
                case Member: return itsMemberItBegin[itsIndex].value;
                default:
                    throw cereal::Exception("YamlInputArchive internal error: null or "
                                            "empty iterator to object or array!");
            }
        }

        //! Get the name of the current node, or nullptr if it has no name
        const char* name() const
        {
            if(itsType == Member && (itsMemberItBegin + itsIndex) != itsMemberItEnd)
                return itsMemberItBegin[itsIndex].name.GetString();
            else
                return nullptr;
        }

        inline void search(const char* searchName)
        {
            const auto len   = std::strlen(searchName);
            size_t     index = 0;
            for(auto it = itsMemberItBegin; it != itsMemberItEnd; ++it, ++index)
            {
                const auto currentName = it->name.GetString();
                if((std::strncmp(searchName, currentName, len) == 0) &&
                   (std::strlen(currentName) == len))
                {
                    itsIndex = index;
                    return;
                }
            }

            throw Exception("YAML Parsing failed - provided NVP (" +
                            std::string(searchName) + ") not found");
        }

    private:
        MemberIterator itsMemberItBegin,
            itsMemberItEnd;             //!< The member iterator (object)
        ValueIterator itsValueItBegin;  //!< The value iterator (array)
        size_t        itsIndex;         //!< The current index of this iterator
        enum Type
        {
            Value,
            Member,
            Null_
        } itsType;  //!< Whether this holds values (array) or members (objects) or
                    //!< nothing
    };

    inline void search()
    {
        // The name an NVP provided with setNextName()
        if(itsNextName)
        {
            // The actual name of the current node
            auto const actualName = itsIteratorStack.back().name();

            // Do a search if we don't see a name coming up, or if the names don't
            // match
            if(!actualName || std::strcmp(itsNextName, actualName) != 0)
                itsIteratorStack.back().search(itsNextName);
        }

        itsNextName = nullptr;
    }

public:
    void startNode()
    {
        search();

        if(itsIteratorStack.back().value().IsArray())
            itsIteratorStack.emplace_back(itsIteratorStack.back().value().Begin(),
                                          itsIteratorStack.back().value().End());
        else
            itsIteratorStack.emplace_back(itsIteratorStack.back().value().MemberBegin(),
                                          itsIteratorStack.back().value().MemberEnd());
    }

    //! Finishes the most recently started node
    void finishNode()
    {
        itsIteratorStack.pop_back();
        ++itsIteratorStack.back();
    }

    const char* getNodeName() const { return itsIteratorStack.back().name(); }

    //! Sets the name for the next node created with startNode
    void setNextName(const char* name) { itsNextName = name; }

    //! Loads a value from the current node - small signed overload
    template <class T, traits::EnableIf<std::is_signed<T>::value,
                                        sizeof(T) < sizeof(int64_t)> = traits::sfinae>
    inline void loadValue(T& val)
    {
        search();

        val = static_cast<T>(itsIteratorStack.back().value().GetInt());
        ++itsIteratorStack.back();
    }

    //! Loads a value from the current node - small unsigned overload
    template <class T,
              traits::EnableIf<std::is_unsigned<T>::value, sizeof(T) < sizeof(uint64_t),
                               !std::is_same<bool, T>::value> = traits::sfinae>
    inline void loadValue(T& val)
    {
        search();

        val = static_cast<T>(itsIteratorStack.back().value().GetUint());
        ++itsIteratorStack.back();
    }

    //! Loads a value from the current node - bool overload
    void loadValue(bool& val)
    {
        search();
        val = itsIteratorStack.back().value().GetBool();
        ++itsIteratorStack.back();
    }
    //! Loads a value from the current node - int64 overload
    void loadValue(int64_t& val)
    {
        search();
        val = itsIteratorStack.back().value().GetInt64();
        ++itsIteratorStack.back();
    }
    //! Loads a value from the current node - uint64 overload
    void loadValue(uint64_t& val)
    {
        search();
        val = itsIteratorStack.back().value().GetUint64();
        ++itsIteratorStack.back();
    }
    //! Loads a value from the current node - float overload
    void loadValue(float& val)
    {
        search();
        val = static_cast<float>(itsIteratorStack.back().value().GetDouble());
        ++itsIteratorStack.back();
    }
    //! Loads a value from the current node - double overload
    void loadValue(double& val)
    {
        search();
        val = itsIteratorStack.back().value().GetDouble();
        ++itsIteratorStack.back();
    }
    //! Loads a value from the current node - string overload
    void loadValue(std::string& val)
    {
        search();
        val = itsIteratorStack.back().value().GetString();
        ++itsIteratorStack.back();
    }
    //! Loads a nullptr from the current node
    void loadValue(std::nullptr_t&)
    {
        search();
        CEREAL_YAML_ASSERT(itsIteratorStack.back().value().IsNull());
        ++itsIteratorStack.back();
    }

// Special cases to handle various flavors of long, which tend to conflict with
// the int32_t or int64_t on various compiler/OS combinations.  MSVC doesn't need any of
// this.
#ifndef _MSC_VER
private:
    //! 32 bit signed long loading from current node
    template <class T>
    inline typename std::enable_if<
        sizeof(T) == sizeof(std::int32_t) && std::is_signed<T>::value, void>::type
    loadLong(T& l)
    {
        loadValue(reinterpret_cast<std::int32_t&>(l));
    }

    //! non 32 bit signed long loading from current node
    template <class T>
    inline typename std::enable_if<
        sizeof(T) == sizeof(std::int64_t) && std::is_signed<T>::value, void>::type
    loadLong(T& l)
    {
        loadValue(reinterpret_cast<std::int64_t&>(l));
    }

    //! 32 bit unsigned long loading from current node
    template <class T>
    inline typename std::enable_if<
        sizeof(T) == sizeof(std::uint32_t) && !std::is_signed<T>::value, void>::type
    loadLong(T& lu)
    {
        loadValue(reinterpret_cast<std::uint32_t&>(lu));
    }

    //! non 32 bit unsigned long loading from current node
    template <class T>
    inline typename std::enable_if<
        sizeof(T) == sizeof(std::uint64_t) && !std::is_signed<T>::value, void>::type
    loadLong(T& lu)
    {
        loadValue(reinterpret_cast<std::uint64_t&>(lu));
    }

public:
    //! Serialize a long if it would not be caught otherwise
    template <class T>
    inline typename std::enable_if<std::is_same<T, long>::value &&
                                       sizeof(T) >= sizeof(std::int64_t) &&
                                       !std::is_same<T, std::int64_t>::value,
                                   void>::type
    loadValue(T& t)
    {
        loadLong(t);
    }

    //! Serialize an unsigned long if it would not be caught otherwise
    template <class T>
    inline typename std::enable_if<std::is_same<T, unsigned long>::value &&
                                       sizeof(T) >= sizeof(std::uint64_t) &&
                                       !std::is_same<T, std::uint64_t>::value,
                                   void>::type
    loadValue(T& t)
    {
        loadLong(t);
    }
#endif  // _MSC_VER

private:
    //! Convert a string to a long long
    void stringToNumber(std::string const& str, long long& val) { val = std::stoll(str); }
    //! Convert a string to an unsigned long long
    void stringToNumber(std::string const& str, unsigned long long& val)
    {
        val = std::stoull(str);
    }
    //! Convert a string to a long double
    void stringToNumber(std::string const& str, long double& val)
    {
        val = std::stold(str);
    }

public:
    //! Loads a value from the current node - long double and long long overloads
    template <
        class T,
        traits::EnableIf<
            std::is_arithmetic<T>::value, !std::is_same<T, long>::value,
            !std::is_same<T, unsigned long>::value, !std::is_same<T, std::int64_t>::value,
            !std::is_same<T, std::uint64_t>::value,
            (sizeof(T) >= sizeof(long double) || sizeof(T) >= sizeof(long long))> =
            traits::sfinae>
    inline void loadValue(T& val)
    {
        std::string encoded;
        loadValue(encoded);
        stringToNumber(encoded, val);
    }

    //! Loads the size for a SizeTag
    void loadSize(size_type& size)
    {
        if(itsIteratorStack.size() == 1)
            size = itsDocument.Size();
        else
            size = (itsIteratorStack.rbegin() + 1)->value().Size();
    }

    //! @}

private:
    const char*           itsNextName;       //!< Next name set by NVP
    ReadStream            itsReadStream;     //!< Rapidyaml write stream
    std::vector<Iterator> itsIteratorStack;  //!< 'Stack' of rapidYAML iterators
};
*/

class YamlInputArchive;

//======================================================================================//
// YAMLArchive prologue and epilogue functions
//======================================================================================//

//======================================================================================//
//! Prologue for NVPs for YAML archives
/*! NVPs do not start or finish nodes - they just set up the names */
template <class T, typename W>
inline void
prologue(YamlOutputArchive&, NameValuePair<T> const&)
{}

//! Prologue for NVPs for YAML archives
template <class T>
inline void
prologue(YamlInputArchive&, NameValuePair<T> const&)
{}

//======================================================================================//
//! Epilogue for NVPs for YAML archives
/*! NVPs do not start or finish nodes - they just set up the names */
template <class T>
inline void
epilogue(YamlOutputArchive&, NameValuePair<T> const&)
{}
//! Epilogue for NVPs for YAML archives
/*! NVPs do not start or finish nodes - they just set up the names */
template <class T>
inline void
epilogue(YamlInputArchive&, NameValuePair<T> const&)
{}

//======================================================================================//
//! Prologue for deferred data for YAML archives
/*! Do nothing for the defer wrapper */
template <class T>
inline void
prologue(YamlOutputArchive&, DeferredData<T> const&)
{}

//! Prologue for deferred data for YAML archives
template <class T>
inline void
prologue(YamlInputArchive&, DeferredData<T> const&)
{}

//======================================================================================//
//! Epilogue for deferred for YAML archives
/*! NVPs do not start or finish nodes - they just set up the names */
template <class T>
inline void
epilogue(YamlOutputArchive&, DeferredData<T> const&)
{}

//! Epilogue for deferred for YAML archives
/*! Do nothing for the defer wrapper */
template <class T>
inline void
epilogue(YamlInputArchive&, DeferredData<T> const&)
{}

//======================================================================================//
//! Prologue for SizeTags for YAML archives
/*! SizeTags are strictly ignored for YAML, they just indicate
    that the current node should be made into an array */
template <class T>
inline void
prologue(YamlOutputArchive& ar, SizeTag<T> const&)
{
    ar.makeArray();
}

//! Prologue for SizeTags for YAML archives
template <class T>
inline void
prologue(YamlInputArchive&, SizeTag<T> const&)
{}

//======================================================================================//
//! Epilogue for SizeTags for YAML archives
/*! SizeTags are strictly ignored for YAML */
template <class T>
inline void
epilogue(YamlOutputArchive&, SizeTag<T> const&)
{}

//! Epilogue for SizeTags for YAML archives
template <class T>
inline void
epilogue(YamlInputArchive&, SizeTag<T> const&)
{}

//======================================================================================//
//! Prologue for all other types for YAML archives (except minimal types)
/*! Starts a new node, named either automatically or by some NVP,
    that may be given data by the type about to be archived

    Minimal types do not start or finish nodes */
template <class T,
          traits::EnableIf<
              !std::is_arithmetic<T>::value,
              !traits::has_minimal_base_class_serialization<
                  T, traits::has_minimal_output_serialization, YamlOutputArchive>::value,
              !traits::has_minimal_output_serialization<T, YamlOutputArchive>::value> =
              traits::sfinae>
inline void
prologue(YamlOutputArchive& ar, T const&)
{
    ar.startNode();
}
/*
//! Prologue for all other types for YAML archives
template <class T,
          traits::EnableIf<
              !std::is_arithmetic<T>::value,
              !traits::has_minimal_base_class_serialization<
                  T, traits::has_minimal_input_serialization, YamlInputArchive>::value,
              !traits::has_minimal_input_serialization<T, YamlInputArchive>::value> =
              traits::sfinae>
inline void
prologue(YamlInputArchive& ar, T const&)
{
    ar.startNode();
}
*/
//======================================================================================//
//! Epilogue for all other types other for YAML archives (except minimal types)
/*! Finishes the node created in the prologue

    Minimal types do not start or finish nodes */
template <class T,
          traits::EnableIf<
              !std::is_arithmetic<T>::value,
              !traits::has_minimal_base_class_serialization<
                  T, traits::has_minimal_output_serialization, YamlOutputArchive>::value,
              !traits::has_minimal_output_serialization<T, YamlOutputArchive>::value> =
              traits::sfinae>
inline void
epilogue(YamlOutputArchive& ar, T const&)
{
    ar.finishNode();
}
/*
//! Epilogue for all other types other for YAML archives
template <class T,
          traits::EnableIf<
              !std::is_arithmetic<T>::value,
              !traits::has_minimal_base_class_serialization<
                  T, traits::has_minimal_input_serialization, YamlInputArchive>::value,
              !traits::has_minimal_input_serialization<T, YamlInputArchive>::value> =
              traits::sfinae>
inline void
epilogue(YamlInputArchive& ar, T const&)
{
    ar.finishNode();
}
*/
//======================================================================================//
//! Prologue for arithmetic types for YAML archives
inline void
prologue(YamlOutputArchive& ar, std::nullptr_t const&)
{
    ar.writeName();
}
/*
//! Prologue for arithmetic types for YAML archives
inline void
prologue(YamlInputArchive&, std::nullptr_t const&)
{}
*/
//======================================================================================//
//! Epilogue for arithmetic types for YAML archives
inline void
epilogue(YamlOutputArchive&, std::nullptr_t const&)
{}
/*
//! Epilogue for arithmetic types for YAML archives
inline void
epilogue(YamlInputArchive&, std::nullptr_t const&)
{}
*/
//======================================================================================//
//! Prologue for arithmetic types for YAML archives
template <class T, traits::EnableIf<std::is_arithmetic<T>::value> = traits::sfinae>
inline void
prologue(YamlOutputArchive& ar, T const&)
{
    ar.writeName();
}

//! Prologue for arithmetic types for YAML archives
template <class T, traits::EnableIf<std::is_arithmetic<T>::value> = traits::sfinae>
inline void
prologue(YamlInputArchive&, T const&)
{}

//======================================================================================//
//! Epilogue for arithmetic types for YAML archives
template <class T, traits::EnableIf<std::is_arithmetic<T>::value> = traits::sfinae>
inline void
epilogue(YamlOutputArchive&, T const&)
{}

//! Epilogue for arithmetic types for YAML archives
template <class T, traits::EnableIf<std::is_arithmetic<T>::value> = traits::sfinae>
inline void
epilogue(YamlInputArchive&, T const&)
{}

//======================================================================================//
//! Prologue for strings for YAML archives
template <class CharT, class Traits, class Alloc>
inline void
prologue(YamlOutputArchive& ar, std::basic_string<CharT, Traits, Alloc> const&)
{
    ar.writeName();
}

//! Prologue for strings for YAML archives
template <class CharT, class Traits, class Alloc>
inline void
prologue(YamlInputArchive&, std::basic_string<CharT, Traits, Alloc> const&)
{}

//======================================================================================//
//! Epilogue for strings for YAML archives
template <class CharT, class Traits, class Alloc>
inline void
epilogue(YamlOutputArchive&, std::basic_string<CharT, Traits, Alloc> const&)
{}

//! Epilogue for strings for YAML archives
template <class CharT, class Traits, class Alloc>
inline void
epilogue(YamlInputArchive&, std::basic_string<CharT, Traits, Alloc> const&)
{}

//======================================================================================//
// Common YAMLArchive serialization functions
//======================================================================================//
//! Serializing NVP types to YAML
template <class T>
inline void
CEREAL_SAVE_FUNCTION_NAME(YamlOutputArchive& ar, NameValuePair<T> const& t)
{
    ar.setNextName(t.name);
    ar(t.value);
}
/*
template <class T>
inline void
CEREAL_LOAD_FUNCTION_NAME(YamlInputArchive& ar, NameValuePair<T>& t)
{
    ar.setNextName(t.name);
    ar(t.value);
}
*/
//! Saving for nullptr to YAML
inline void
CEREAL_SAVE_FUNCTION_NAME(YamlOutputArchive& ar, std::nullptr_t const& t)
{
    ar.saveValue(t);
}
/*
//! Loading arithmetic from YAML
inline void
CEREAL_LOAD_FUNCTION_NAME(YamlInputArchive& ar, std::nullptr_t& t)
{
    ar.loadValue(t);
}
*/
//! Saving for arithmetic to YAML
template <class T, traits::EnableIf<std::is_arithmetic<T>::value> = traits::sfinae>
inline void
CEREAL_SAVE_FUNCTION_NAME(YamlOutputArchive& ar, T const& t)
{
    ar.saveValue(t);
}
/*
//! Loading arithmetic from YAML
template <class T, traits::EnableIf<std::is_arithmetic<T>::value> = traits::sfinae>
inline void
CEREAL_LOAD_FUNCTION_NAME(YamlInputArchive& ar, T& t)
{
    ar.loadValue(t);
}
*/
//! saving string to YAML
template <class CharT, class Traits, class Alloc>
inline void
CEREAL_SAVE_FUNCTION_NAME(YamlOutputArchive&                             ar,
                          std::basic_string<CharT, Traits, Alloc> const& str)
{
    ar.saveValue(str);
}
/*
//! loading string from YAML
template <class CharT, class Traits, class Alloc>
inline void
CEREAL_LOAD_FUNCTION_NAME(YamlInputArchive&                        ar,
                          std::basic_string<CharT, Traits, Alloc>& str)
{
    ar.loadValue(str);
}
*/
//======================================================================================//
//! Saving SizeTags to YAML
template <class T>
inline void
CEREAL_SAVE_FUNCTION_NAME(YamlOutputArchive&, SizeTag<T> const&)
{
    // nothing to do here, we don't explicitly save the size
}
/*
//! Loading SizeTags from YAML
template <class T>
inline void
CEREAL_LOAD_FUNCTION_NAME(YamlInputArchive& ar, SizeTag<T>& st)
{
    ar.loadSize(st.size);
}
*/
}  // namespace cereal

// register archives for polymorphic support
CEREAL_REGISTER_ARCHIVE(cereal::YamlInputArchive)
CEREAL_REGISTER_ARCHIVE(cereal::YamlOutputArchive)

// tie input and output archives together
CEREAL_SETUP_ARCHIVE_TRAITS(cereal::YamlInputArchive, cereal::YamlOutputArchive)
