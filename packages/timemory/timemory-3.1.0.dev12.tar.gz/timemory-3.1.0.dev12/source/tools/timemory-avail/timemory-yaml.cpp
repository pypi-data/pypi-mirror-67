//  MIT License
//
//  Copyright (c) 2020, The Regents of the University of California,
// through Lawrence Berkeley National Laboratory (subject to receipt of any
// required approvals from the U.S. Dept. of Energy).  All rights reserved.
//
//  Permission is hereby granted, free of charge, to any person obtaining a copy
//  of this software and associated documentation files (the "Software"), to
//  deal in the Software without restriction, including without limitation the
//  rights to use, copy, modify, merge, publish, distribute, sublicense, and
//  copies of the Software, and to permit persons to whom the Software is
//  furnished to do so, subject to the following conditions:
//
//  The above copyright notice and this permission notice shall be included in
//  all copies or substantial portions of the Software.
//
//  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
//  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
//  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
//  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
//  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
//  FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
//  IN THE SOFTWARE.

//
#include "timemory/environment.hpp"
#include "timemory/settings.hpp"
#include "timemory/utility/argparse.hpp"
#include "timemory/utility/yaml.hpp"

#include <algorithm>
#include <array>
#include <iomanip>
#include <iostream>
#include <ostream>
#include <sstream>
#include <tuple>
#include <vector>

using namespace tim;
using string_t       = std::string;
using stringstream_t = std::stringstream;
using str_vec_t      = std::vector<string_t>;
using info_type      = std::tuple<string_t, bool, str_vec_t>;

template <typename Tp, size_t N>
using array_t = std::array<Tp, N>;

//--------------------------------------------------------------------------------------//

char global_delim = '|';
bool markdown     = false;
bool alphabetical = false;
bool all_info     = false;
int  padding      = 4;

static constexpr size_t num_settings_options = 3;

template <size_t N = num_settings_options>
void
write_settings_info(std::ostream&, const array_t<bool, N>& = array_t<bool, N>{},
                    const array_t<bool, N>&     = array_t<bool, N>{},
                    const array_t<string_t, N>& = array_t<string_t, N>{});

//--------------------------------------------------------------------------------------//

enum
{
    FNAME = 0,
    ENUM  = 1,
    LANG  = 2,
    CID   = 3,
    DESC  = 4,
    VAL   = 5
};

//--------------------------------------------------------------------------------------//

int
main(int argc, char** argv)
{
    array_t<bool, 6>     options  = { false, false, false, false, false, false };
    array_t<string_t, 6> fields   = {};
    array_t<bool, 6>     use_mark = {};

    fields[CID]   = "STRING_IDS";
    fields[VAL]   = "VALUE_TYPE";
    fields[DESC]  = "DESCRIPTION";
    fields[ENUM]  = "ENUMERATION";
    fields[LANG]  = "C++ ALIAS / PYTHON ENUMERATION";
    fields[FNAME] = "FILENAME";

    use_mark[CID]   = false;
    use_mark[VAL]   = true;
    use_mark[DESC]  = false;
    use_mark[ENUM]  = true;
    use_mark[LANG]  = true;
    use_mark[FNAME] = false;

    bool include_settings    = false;
    bool include_components  = false;
    bool include_hw_counters = false;

    std::string file = "";

    tim::argparse::argument_parser parser("timemory-avail");

    parser.enable_help();
    parser.add_argument({ "-a", "--all" }, "Print all available info");
    parser.add_argument({ "-A", "--alphabetical" }, "Sort the output alphabetically");
    parser
        .add_argument({ "-d", "--description" },
                      "Output the description for the component")
        .count(0);
    parser.add_argument({ "-e", "--enum" }, "Display the enumeration ID").count(0);
    parser.add_argument({ "-f", "--filename" }, "Output the filename for the component")
        .count(0);
    parser
        .add_argument({ "-l", "--language-types" },
                      "Display the language-based alias/accessors")
        .count(0);
    parser.add_argument({ "-s", "--string" }, "Display all acceptable string identifiers")
        .count(0);
    parser.add_argument({ "-v", "--value" }, "Output the value type for the component")
        .count(0);
    parser.add_argument({ "-S", "--settings" }, "Display the runtime settings").count(0);
    parser.add_argument({ "-C", "--components" }, "Only display the components data")
        .count(0);
    parser.add_argument({ "-M", "--markdown" }, "Write data in markdown").count(0);
    parser.add_argument({ "-H", "--hw-counters" },
                        "Write the available hardware counters");
    parser.add_argument({ "-O", "--output" }, "Write results to file").count(1);

    auto err = parser.parse(argc, argv);
    if(err)
        std::cerr << err << std::endl;

    if(err || parser.exists("h"))
    {
        parser.print_help();
        return EXIT_FAILURE;
    }

    if(parser.exists("a"))
        all_info = true;

    if(parser.exists("A"))
        alphabetical = true;

    if(parser.exists("f"))
        options[FNAME] = !options[FNAME];

    if(parser.exists("d"))
        options[DESC] = !options[DESC];

    if(parser.exists("v"))
        options[VAL] = !options[VAL];

    if(parser.exists("e"))
        options[ENUM] = !options[ENUM];

    if(parser.exists("l"))
        options[LANG] = !options[LANG];

    if(parser.exists("s"))
        options[CID] = !options[CID];

    if(parser.exists("O"))
        file = parser.get<std::string>("O");

    if(parser.exists("C"))
        include_components = true;

    if(parser.exists("S"))
    {
        include_settings = true;
    }

    if(parser.exists("M"))
    {
        markdown = true;
        padding  = 6;
    }

    if(parser.exists("H"))
    {
        include_hw_counters = true;
        padding             = 6;
    }

    if(!include_components && !include_settings && !include_hw_counters)
    {
        include_components = true;
    }

    std::ostream* os = nullptr;
    std::ofstream ofs;
    if(!file.empty())
    {
        ofs.open(file.c_str());
        if(ofs)
            os = &ofs;
        else
            std::cerr << "Error opening output file: " << file << std::endl;
    }

    if(!os)
        os = &std::cout;

    if(all_info)
    {
        for(auto& itr : options)
            itr = true;
        include_components  = true;
        include_settings    = true;
        include_hw_counters = true;
    }

    write_settings_info(*os, { options[VAL], options[LANG], options[DESC] });

    return 0;
}

//--------------------------------------------------------------------------------------//

struct test
{
    double      fval = 1.0;
    std::string fkey = "mylabel";

    template <typename Archive>
    void serialize(Archive& ar, const unsigned int)
    {
        ar(cereal::make_nvp("fval", fval));
        ar(cereal::make_nvp("fkey", fkey));
    }
};

//--------------------------------------------------------------------------------------//

template <size_t N>
void
write_settings_info(std::ostream& os, const array_t<bool, N>& opts,
                    const array_t<bool, N>&, const array_t<string_t, N>&)
{
    static_assert(N >= num_settings_options, "Error! Too few settings options + fields");

    using archive_type = cereal::YamlOutputArchive;

    std::stringstream ss;
    {
        archive_type settings_archive(ss);
        test         _t;
        settings_archive(cereal::make_nvp("test", _t));
    }

    std::ofstream ofs("settings.yaml");
    ofs << ss.str() << std::endl;
    ofs.close();

    std::cout << std::endl;
    std::cout << ss.str() << std::endl;
    std::cout << std::endl;
}

//--------------------------------------------------------------------------------------//
