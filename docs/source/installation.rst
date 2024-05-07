..
   Installation
   =====
   
   .. _installation:
   
   Installation
   ------------
   
   To use Lumache, first install it using pip:
   
   .. code-block:: console
   
      (.venv) $ pip install lumache
   
   Creating recipes
   ----------------
   
   To retrieve a list of random ingredients,
   you can use the ``lumache.get_random_ingredients()`` function:
   
   .. autofunction:: lumache.get_random_ingredients
   
   The ``kind`` parameter should be either ``"meat"``, ``"fish"``,
   or ``"veggies"``. Otherwise, :py:func:`lumache.get_random_ingredients`
   will raise an exception.
   
   .. autoexception:: lumache.InvalidKindError
   
   For example:
   
   >>> import lumache
   >>> lumache.get_random_ingredients()
   ['shells', 'gorgonzola', 'parsley']

Installation
=====
.. _installation


The project is built in Python using various libraries as listed above and PostgreSQL.

Cloning the repository using Git
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Guide to Cloning the repository via `Github Website <https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository>`_

Python Link and Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

These are the links to download Python and the language documentation:

- `Python Download <https://www.python.org/downloads/>`_
- `Python Documentation <https://docs.python.org/3/>`_

The Python libraries used:
~~~~~~~~~~~~~~~~~~~~~~~~~~

Psycopg2: Used to connect Python to a PostgreSQL database and run queries in Python: `Documentation <https://www.psycopg.org/docs/>`_

Kivy: Used to create the GUI for the project: `Documentation <https://kivy.org/doc/>`_

Typing: (Not Required) Used to improve comments and Type Scripting to the program: `Documentation <https://docs.python.org/3/library/typing.html>`_

Installation Guide For Python Libraries:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For installing the various Python Libraries, we recommend using the package manager `pip <https://pypi.org/project/pip/>`_

To install all required libraries for the timetable generator to work, please use the following command from a terminal where its directory is the root director of the program.

::

    pip install -r requirements.txt

- Kivy

::

    pip install kivy

Installation Guide For PostgreSQL
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Download link for PostgreSQL: `PostgreSQL Download <https://www.postgresql.org/download/>`_

We recommend downloading PostgreSQL locally to your machine as it will make running the program easier, this will also allow you more control and ability to test any changes made to the database.

Download Steps:

1. Download the correct and most recent download for your OS (Windows, Linux, MacOS, etc...)
2. Once the PostgreSQL has downloaded, navigate to your start / apps section of your computer / laptop / etc and search for ``pgAdmin_4``.
3. On your first time opening ``pgAdmin_4`` you will need to set a password, remember the password, you will need this password for configuration.
4. The setup should now be complete.

Final setup
~~~~~~~~~~~

Once all the dependencies have been downloaded and successfully installed, you will need to complete some further steps before the project can run.

Final Steps:

1. Navigate to the ``Config.py`` file / Navigate to the ``databaseManager.py`` file
2. You will need to enter the following information:
   - host --> The name of the server the database is hosted on.
   - dbname --> The name of the database the data is being stored on.
   - password --> Your password, this is the same password you used when first opening ``pgAdmin_4``.

3. Save these changes in the file.

After making these changes, the project should run.

