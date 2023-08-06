**********
POP_DARWIN
**********
**Grains, execution modules, and state modules common to all darwin systems**

INSTALLATION
============

Install idem-darwin directly from pip::

    pip install idem-darwin

DEVELOPMENT INSTALLATION
========================


Clone the `idem_darwin` repo and install with pip::

    git clone https://gitlab.com/saltstack/pop/idem-darwin.git idem_darwin
    pip install -e idem_darwin

EXECUTION
=========
After installation the `corn` command should now be available

TESTING
=======
install `requirements-test.txt` with pip and run pytest::

    pip install -r idem_darwin/requirements-test.txt
    pytest idem_darwin/tests

VERTICAL APP-MERGING
====================
Instructions for extending pop-darwin into an OS-specific pop project

Install pop::

    pip install --upgrade pop

Create a new directory for the project::

    mkdir pop_{specific_darwin_os}
    cd pop_{specific_darwin_os}


Use `pop-seed` to generate the structure of a project that extends `corn` and `idem`::

    pop-seed -t v pop_{specific_darwin_os} -d corn exec states

* "-t v" specifies that this is a vertically app-merged project
*  "-d corn exec states" says that we want to implement the dynamic names of "corn", "exec", and "states"

Add "idem_darwin" to the requirements.txt::

    echo "idem_darwin @ git+https://gitlab.com/saltstack/pop/idem_darwin.git" >> requirements.txt

And that's it!  Go to town making corn, execution modules, and state modules specific to your specific darwin-based platform.
Follow the conventions you see in idem_darwin.

For information about running idem states and execution modules check out
https://idem.readthedocs.io
