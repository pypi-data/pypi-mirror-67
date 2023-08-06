Development roadmap
===================

This page describes some possible future enhancements to :mod:`sdmx`.
For current development priorities, see the list of `GitHub milestones <https://github.com/khaeru/sdmx/milestones>`_ and issues/PRs targeted to each.
Contributions are welcome!

Using pd.DataFrame for internal storage
----------------------------------------

:mod:`sdmx` handles :class:`Observations <sdmx.model.Observation>` as individual object instances.
An alternative is to use :mod:`pandas` or other data structures internally.
See:

- sdmx/experimental.py for a partial mock-up of such code, and
- tests/test_experimental.py for tests.

Choosing either the current or experimental DataSet as a default should be based on detailed performance (memory and time) evaluation under a variety of use-cases.
To that end, note that the experimental DataSet involves three conversions:

1. a reader parses the XML or JSON source, creates Observation instances, and adds them using DataSet.add_obs()
2. experimental.DataSet.add_obs() populates a pd.DataFrame from these Observations, but discards them.
3. experimental.DataSet.obs() creates new Observation instances.

For a fair comparison, the API between the readers and DataSet could be changed to eliminate the round trip in #1/#2, but *without* sacrificing the data model consistency provided by pydantic on Observation instances.

Optimize parsing
----------------

The current readers implement depth-first parsing of XML or JSON SDMX messages.
This ensures the returned objects confirm rigorously to the SDMX Information Model, but can be slow for very large messages (both Structure and Data).

There are some ways this performance could be improved:

- Create-on-access: don't immediately parse an entire document, but only as requested to construct other objects.
  This would make some internals more complex:

  - Observation association with GroupKeys is determined by comparing the Observation key with the GroupKey.
    In order to have a complete list of all Observations associated with a GroupKey, at least the dimension of each Observation would need to be parsed immediately.

  - In sdmx.sdmxml.reader, references are determined to be internal or external by checking against an _index of already-parsed objects.
    This index would need to represent existing-but-not-parsed objects.

- Parallelize parsing, e.g. at the level of Series or other mostly-separate collections of objects.

SDMX features & miscellaneous
-----------------------------

- sdmx.api.Request._resources only contains a small subset of: https://ec.europa.eu/eurostat/web/sdmx-web-services/rest-sdmx-2.1 (see "NOT SUPPORTED OPERATIONS"); provide the rest.

- Get a set of API keys for testing UNESCO and encrypt them for use in CI: https://docs.travis-ci.com/user/encryption-keys/

- Serialize :class:`Message` objects SDMX-CSV (simplest), -JSON, or -ML (most complex).

- Use the `XML Schema <https://en.wikipedia.org/wiki/XML_Schema_(W3C)>`_ definitions of SDMX-ML to validate messages and snippets.

- SOAP APIs. Currently only REST APIs are supported.
  This would allow access to, e.g., a broader set of :ref:`IMF` data.

- Support SDMX-ML 2.0.
  Several data providers still exist which only return SDMX-ML 2.0 messages.

- Performance.
  Parsing some messages can be slow.
  Install pytest-profiling_ and run, for instance::

      $ py.test --profile --profile-svg -k xml_structure_insee
      $ python3 -m pstats prof/combined.prof
      % sort cumulative
      % stats

Inline TODOs
~~~~~~~~~~~~

.. todolist::

.. _pytest-profiling: https://pypi.org/project/pytest-profiling/
