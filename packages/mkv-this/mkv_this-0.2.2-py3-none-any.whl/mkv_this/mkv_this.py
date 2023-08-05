#! /usr/bin/env python3

"""
    mkv-this: input a text file, directory, and/or url, output markovified text.

    Copyright (C) 2020 martianhiatus@riseup.net.

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""


import markovify
import os
import sys
import datetime
import argparse
from .functions import (
    URL,
    convert_html,
    dir_list,
    dir_cat,
    read,
    mkbtext,
    mkbnewline,
    writesentence,
    writeshortsentence,
)

# argparse
def parse_the_args():
    parser = argparse.ArgumentParser(
        prog="mkv-this",
        description="markovify local text files, directory, or URLs and output the results to a local text file.",
        epilog="may you find many prophetic énoncés in your virtual bird guts! Here, this is not at all the becomings that are connected... so if you want to edit it like a bot yourself, it is trivial.\n  '`mkv-this` is a waste product of machine—machine interactions become the historical record.'",
    )
    # positional args:
    parser.add_argument("infile", help="the text file to process.")
    parser.add_argument(
        "outfile",
        nargs="?",
        default="./mkv-output.txt",
        help="the file to save to. if the file is used more than once, subsequent literature will be appended to it. defaults to ./mkv-output.txt.",
    )
    # optional args:
    parser.add_argument(
        "-u",
        "--URL",
        help="infile is a URL. all text it contains will be used.",
        action="store_true",
    )
    parser.add_argument(
        "-d",
        "--directory",
        help="infile is a directory. all text files in it and its subdirectories will be used.",
        action="store_true",
    )
    parser.add_argument(
        "-s",
        "--state-size",
        help="the number of preceeding words used to calculate the probability of the next word. defaults to 2, 1 makes it more random, 3 less so. > 4 will likely have little effect.",
        type=int,
        default=2,
    )
    parser.add_argument(
        "-n",
        "--sentences",
        help="the number of 'sentences' to output. defaults to 5. NB: if your text has no initial caps, a 'sentence' will be a paragraph.",
        type=int,
        default=5,
    )
    parser.add_argument(
        "-l",
        "--length",
        help="set maximum number of characters per sentence.",
        type=int,
    )
    parser.add_argument(
        "-o",
        "--overlap",
        help="the amount of overlap allowed between original and output, expressed as a ratio between 0 and 1. defaults to 0.5",
        type=float,
        default=0.5,
    )
    parser.add_argument(
        "-c",
        "--combine",
        help="provide an another text file to be combined with the first item.",
    )
    parser.add_argument(
        "-C", "--combine-URL", help="provide a URL to be combined with the first item"
    )
    parser.add_argument(
        "-w",
        "--weight",
        help="specify the weight to be given to the text provided with -c or -C. defaults to 1, and the weight of the initial text is 1. 1.5 will place more weight on the second text, 0.5 will place less.",
        type=float,
        default=1,
    )
    parser.add_argument(
        "-f",
        "--well-formed",
        help="enforce 'well_formed': discard sentences containing []{}()"
        "'' from the markov model. use if output is filthy.",
        action="store_true",
    )
    # store_true = default to False.
    parser.add_argument(
        "--newline",
        help="sentences in input file end with newlines rather than full stops.",
        action="store_true",
    )
    # store_true = default to False, True if flagged.
    parser.add_argument(
        "-t",
        "--timestamp",
        help="add date and time to the file before the output.",
        action="store_true",
    )
    parser.add_argument(
        "-p",
        "--save-options",
        help="add a brief summary of options used before the output.",
        action="store_true",
    )

    return parser.parse_args()


# make args avail:
args = parse_the_args()


def main():
    # if a -c/-C, combine it w infile/URL:
    if args.combine or args.combine_URL:
        if args.combine:
            # get raw text as a string for both:
            # infile is URL:
            if args.URL:
                html = URL(args.infile)
                text = convert_html(html)
            # infile is dir:
            elif args.directory:
                matchlist = dir_list(args.infile)
                # place batchfile.txt in user-given directory:
                batchfile = args.infile + os.path.sep + "batchfile.txt"
                dir_cat(matchlist, batchfile)
                text = read(batchfile)
                os.unlink(batchfile)
            # or normal:
            else:
                text = read(args.infile)
            # read -c file:
            ctext = read(args.combine)

        # if -C, combine it w infile/URL:
        elif args.combine_URL:
            # infile is URL:
            if args.URL:
                html = URL(args.infile)
                text = convert_html(html)
            # infile is dir:
            elif args.directory:
                matchlist = dir_list(args.infile)
                # place batchfile.txt in args.infile:
                batchfile = args.infile + os.path.sep + "batchfile.txt"
                dir_cat(matchlist, batchfile)
                text = read(batchfile)
                os.unlink(batchfile)
            # or normal:
            else:
                text = read(args.infile)
            # now combine_URL:
            html = URL(args.combine_URL)
            ctext = convert_html(html)

        # build the models + a combined model:
        # with --newline:
        if args.newline:
            text_model = mkbnewline(text, args.state_size, args.well_formed)
            ctext_model = mkbnewline(ctext, args.state_size, args.well_formed)
        # no --newline:
        else:
            text_model = mkbtext(text, args.state_size, args.well_formed)
            ctext_model = mkbtext(ctext, args.state_size, args.well_formed)

        combo_model = markovify.combine([text_model, ctext_model], [1, args.weight])

    # if no -c/-C, do normal:
    else:
        # Get raw text as string.
        # either URL:
        if args.URL:
            html = URL(args.infile)
            text = convert_html(html)
        elif args.directory:
            matchlist = dir_list(args.infile)
            # place batchfile.txt in user-given directory:
            batchfile = args.infile + os.path.sep + "batchfile.txt"
            dir_cat(matchlist, batchfile)
            text = read(batchfile)
            os.unlink(batchfile)
        # or local file:
        else:
            text = read(args.infile)

        # Build the model:
        # if --newline:
        if args.newline:
            text_model = mkbnewline(text, args.state_size, args.well_formed)
        # no --newline:
        else:
            text_model = mkbtext(text, args.state_size, args.well_formed)

    # merge the strains to prepare to write:
    if args.combine or args.combine_URL:
        model = combo_model
    else:
        model = text_model
    if args.length:
        write = writeshortsentence
    else:
        write = writesentence

    with open(args.outfile, "a") as outp:
        # optional print timestamp header:
        if args.timestamp:
            outp.write(str(datetime.datetime.now()) + ":\n")
        # optional print options used header:
        if args.save_options:
            outp.write("input: " + vars(args)["infile"] + " | ")
            if args.combine:
                outp.write("comb: " + vars(args)["combine"] + " | ")
            if args.combine_URL:
                outp.write("comb: " + vars(args)["combine_URL"] + " | ")
            if args.combine or args.combine_URL:
                outp.write("weight: " + str(vars(args)["weight"]) + " | ")
                outp.write("overlap: " + str(vars(args)["overlap"]) + " | ")
            outp.write("state size: " + str(vars(args)["state_size"]) + "\n")
        outp.write("\n")

    # write it!
    write(model, args.sentences, args.outfile, args.overlap, args.length)

    # wrapping up:
    print("\n:                :\n")
    for key, value in vars(args).items():
        print(": " + key.ljust(15, " ") + ":  " + str(value).ljust(10))
    if os.path.isfile(args.outfile):
        print(
            "\n:  literary genius has been written to the file "
            + args.outfile
            + ". thanks for playing!\n\n: 'Here, this is not at all the becomings that are connected... so if you want to edit it like a bot yourself, it is trivial. Yes, although your very smile suggests that this Armenian enclave is not at all the becomings that are connected...'"
        )
    else:
        print(
            ": mkv-this ran but did NOT create an output file as requested. this is a very regrettable and dangerous situation. contact the package maintainer asap. soz!"
        )

    sys.exit()
