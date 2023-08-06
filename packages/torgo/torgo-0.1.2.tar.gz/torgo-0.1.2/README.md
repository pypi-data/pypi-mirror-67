<p align="center"><img src="torgo.jpg" /></p>

![](https://github.com/criswell/torgo/workflows/CI/badge.svg)

Torgo is the system-wide org file manager. It allows you to create org-mode
files that are associated with whatever directory you are in, but which are
managed externally.

# Usage

```
usage: torgo [-h] [-l] [-t] [-i] [-p] [command] [param]

Org-file anywhere, managed

positional arguments:
  command      The command to run
  param        Optional param for commands, see commands list for more
               information

optional arguments:
  -h, --help   show this help message and exit
  -l, --list   List the commands available
  -t, --this   Use 'this' directory, don't attempt to find org file in parents
  -i, --init   Force a re-init of the configuration
  -p, --prune  Prune the current org file (delete it)
```

Wherever you run torgo, torgo will create a managed org-mode file for the
directory you are in. This org-mode file will be stored in a central location,
but will be associated with the directory torgo was called from.

## Configuration

When torgo is first ran, it will walk you through a configuration file
creation process. This configuration file defaults to `~/.torgo.cfg`, but you
can override that with the `$TORGO_CFG` environment variable.

The config file defines the following settings:

* `org_dir` : This is the path to where your org files will go. It defaults
to `~/.torgo/`.
* `editor` : This is your desired text editor. If blank, will attempt to use
`$EDITOR` from your environment.
* `ext` : This is the desired org file extension. It defaults to `org`.

You can force torgo to re-initialize the configuration by passing the
`-i`/`--init` option.

## How does it work?

Perhaps the best way to understand how to use torgo, is to see how it works.

When torgo is run, it starts in the current working directory and checks if
an org file entry exists for that directory in its flat database file (by
default, this is `~/.torgo/org_lookup_db.json`). If no org-file is found, it
steps up to the parent directory and checks there. It repeats this until it
either finds an org file or reaches root. If it reaches root, then it takes
the original working directory as the one for the org-mode.

*Note: You can force it to use the current working directory by passing the
`-t`/`--this` parameter.*

Once it has the appropriate org-mode file it fires up your editor of choice
on that file. You edit the file, take your notes or whatever, and save it.

The next time you fire up torgo in that same directory (or in a sub-directory)
it will load the same org-mode file.

### Tagging

Each org file can be tagged with any number of tags. To set or unset the tags,
use the `tag` command. Tags are a comma-separated list of parameters after
the tag command. Tags with a `.` (period/dot) prefix will be unset. To list
the tags for a given org file, call tag without any parameters.

```
> torgo tag foo,bar,baz
> torgo tag
The tags associated with this org file:
    foo
    bar
    baz
> torgo tag .bar
> torgo tag
The tags associated with this org file:
    foo
    baz
```

Once tagged, you can search for all the paths which have org files associated
with a given list of tags using the `search` command using a list of tags as
its parameter.

```
> torgo search tag=foo,bar
Found 3 records with the following tags:
	foo
	bar

Path: /home/sam/work/torgo | [oss, python, foo]
Path: /home/sam/work/bigdeal | [bar, work]
Path: /home/sam/meh | [oss, github, dotfiles, foo, bar]
```

### Does it have to be org-mode files?

No! Simply change the `ext` in the configuration file to whatever extension
you'd like. Torgo doesn't force any file type on you, it just manages the
files associated with your directories. If you would rather take your notes
in Markdown, plain-text, or anything else, you're free to do so.

# Why is it called Torgo?

For a while, I had been using a `this.org` pattern for my ad-hoc org files.
Say I was in a directory that was a repo for a project I was on and suddenly
needed to take notes- I'd do a `vim .this.org` and write my notes in it. Or
say I was configuring something in the system and needed to take notes on
what I was doing- Again, I'd do a `vim .this.org`.

This pattern worked well because I'd always be able to have contextual org-mode
note files wherever I was. But it had a number of downsides.

For one, it littered my directories with `.this.org` files. If a directory
was a repo, I'd generally have to add `.this.org` to its ignore file. Further,
I'd have no way to easily backup or version control all of my `.this.org` files.

I created a hacky shell script that would let me have system-wide org-mode files
in my home-directory that would be associated by hashes of the directories I
was in. This let me keep my `this.org` pattern, but not litter my directories.
It also let me version control my `this.org` files and back them up easily.

Originally, this shell script was called `torg` (from `this.org`). As I started
refining it, and extending it, I eventually decided I should re-write it in
Python. Since I was a MST3k fan, and since Manos The Hands of Fate is the
greatest movie of all time, it was an easy leap to go from `this.org`, to `torg`,
to `torgo`.
