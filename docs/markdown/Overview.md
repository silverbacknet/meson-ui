---
short-description: Overview of the Meson build GUI
...

# Overview

Meson-UI is a build GUI that is designed to be as user-friendly as
possible without sacrificing performance. The main tool for this is
a Graphical application designed to provide an interactive way to
use the Meson build system commands with out using command line.

Another main idea has been to provide first class support for modern
Meson build system best practices. These include features as varied
as init new templates, setup projects, unit testing, configure. All
of these features should be immediately available to any project
using Meson-UI.

Terminology
--

Meson follows the overall structure of other popular build systems,
such as CMake and GNU Autotools. This means that the build is divided
into two discrete steps: *configure step* and *build step*. The first
step inspects the system, checks for dependencies and does all other
steps necessary to configure the build. It then generates the actual
build system. The second step is simply executing this generated build
system. The end result is a bunch of *build targets*, which are
usually executables and shared and static libraries.

The directory that contains the source code is called the *source
directory*. Correspondingly the directory where the output is written
is called the *build directory*. In other build systems it is common
to have these two be the same directory. This is called an *in-source
build*. The case where the build directory is separate is called an
*out-of-source build*.

What sets Meson apart from most build systems is that it enforces a
separate build directory. All files created by the build system are
put in the build directory. It is actually impossible to do an
in-source build. For people used to building inside their source tree,
this may seem like a needless complication. However there are several
benefits to doing only out-of-source builds. These will be explained
in the next chapter.

When the source code is built, a set of *unit tests* is usually
run. They ensure that the program is working as it should. If it does,
the build result can be *installed* after which it is ready for use.
