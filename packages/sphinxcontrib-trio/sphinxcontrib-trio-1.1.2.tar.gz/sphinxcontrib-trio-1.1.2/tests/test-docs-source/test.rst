=====================================
 sphinxcontrib-trio end-to-end tests
=====================================

Each ``note`` in this file is a test case. The ``test_end_to_end``
function in ``test_sphinxcontrib_trio.py`` loops through the rendered
output of each ``note``, and for each one it finds all the "none"
code-blocks, and it makes sure that the contents of that code-block
appears in the html source for the rest of the note.

It also runs all ``warning``\s as tests in the same way, but for these
it checks that they fail. This acts as a check that the test harness
is actually working, and can be used for negative tests.

Currently there is no normalization applied to the HTML. We can add
it later if it turns out to be a problem...

Basic smoke tests
=================

.. note::

   .. function:: foo(bar)
      :noindex:
      :async:

   .. code-block:: none

      <em class="property">await </em><code class="(sig-name )?descname">foo</code>


.. warning::

   .. function:: foo(bar)
      :noindex:

   .. code-block:: none

      <em class="property">await </em><code class="(sig-name )?descname">foo</code>


Check all the formatting logic
==============================

.. note::

   .. method:: foo(bar)
      :noindex:
      :abstractmethod:
      :staticmethod:
      :async:

   .. code-block:: none

      <em class="property">abstractmethod staticmethod await </em><code class="(sig-name )?descname">foo</code>


.. note::

   .. method:: foo(bar)
      :noindex:
      :classmethod:

   .. code-block:: none

      <em class="property">classmethod </em><code class="(sig-name )?descname">foo</code>


.. note::

   .. function:: foo(bar)
      :noindex:
      :with:

   .. code-block:: none

      <em class="property">with </em><code class="(sig-name )?descname">foo</code>


.. note::

   .. method:: foo(bar)
      :noindex:
      :with: baz

   .. code-block:: none

      <em class="property">with </em><code class="(sig-name )?descname">foo</code><span class="sig-paren">\(</span><em( class="sig-param")?>(<span class="n">)?bar(</span>)?</em><span class="sig-paren">\)</span><em class="property">&nbsp;as baz</em>

.. note::

   .. method:: foo(bar)
      :noindex:
      :async-with:

   .. code-block:: none

      <em class="property">async with </em><code class="(sig-name )?descname">foo</code>


.. note::

   .. method:: foo(bar)
      :noindex:
      :async-with: baz

   .. code-block:: none

      <em class="property">async with </em><code class="(sig-name )?descname">foo</code><span class="sig-paren">\(</span><em( class="sig-param")?>(<span class="n">)?bar(</span>)?</em><span class="sig-paren">\)</span><em class="property">&nbsp;as baz</em>


This one checks that decorators don't normally have parentheses:

.. note::

   .. decorator:: foo
      :noindex:

   .. code-block:: none

      <code class="(sig-prename )?descclassname">@</code><code class="(sig-name )?descname">foo</code></dt>


But if you do have arguments, they're displayed

.. note::

   .. decorator:: foo(bar)
      :noindex:

   .. code-block:: none

      <code class="(sig-prename )?descclassname">@</code><code class="(sig-name )?descname">foo</code><span class="sig-paren">\(</span><em( class="sig-param")?>(<span class="n">)?bar(</span>)?</em>


Same for properties, in case someone uses `.. method:: :property:`
(instead of the more usual `.. data::`), or sphinx 2.1 uses it for us:

.. note::

  .. method:: foo()
     :noindex:
     :property:

  .. code-block:: none

     <code class="(sig-name )?descname">foo</code></dt>


.. note::

   .. method:: foo(bar)
      :noindex:
      :for:

   .. code-block:: none

      <em class="property">for ... in </em><code class="(sig-name )?descname">foo</code>


.. note::

   .. method:: foo(bar)
      :noindex:
      :for: baz

   .. code-block:: none

      <em class="property">for baz in </em><code class="(sig-name )?descname">foo</code>

.. note::

   .. method:: foo(bar)
      :noindex:
      :async-for:

   .. code-block:: none

      <em class="property">async for ... in </em><code class="(sig-name )?descname">foo</code>


.. note::

   .. method:: foo(bar)
      :noindex:
      :async-for: baz

   .. code-block:: none

      <em class="property">async for baz in </em><code class="(sig-name )?descname">foo</code>


Backwards compatibility directives
==================================

.. note::

   .. decorator:: foo
      :noindex:

   .. code-block:: none

      <code class="(sig-prename )?descclassname">@</code><code class="(sig-name )?descname">foo</code>

.. note::

   .. decoratormethod:: foo
      :noindex:

   .. code-block:: none

      <code class="(sig-prename )?descclassname">@</code><code class="(sig-name )?descname">foo</code>

.. note::

   .. classmethod:: foo(bar)
      :noindex:

   .. code-block:: none

      <em class="property">classmethod </em><code class="(sig-name )?descname">foo</code>

.. note::

   .. staticmethod:: foo(bar)
      :noindex:

   .. code-block:: none

      <em class="property">staticmethod </em><code class="(sig-name )?descname">foo</code>


Autodoc
=======

.. module:: autodoc_examples

Autodoc smoke tests:

.. note::

   .. autofunction:: basic
      :noindex:

   .. code-block:: none

      <code class="(sig-prename )?descclassname">autodoc_examples.</code><code class="(sig-name )?descname">basic</code>

.. warning::

   .. autofunction:: basic
      :noindex:

   .. code-block:: none

      </em><code class="(sig-name )?descname">basic</code>

.. note::

   .. autofunction:: asyncfn
      :noindex:

   .. code-block:: none

      <em class="property">await </em><code class="(sig-prename )?descclassname">autodoc_examples.</code><code class="(sig-name )?descname">asyncfn</code>

We don't bother testing every bizarro combination here, because we
have unit tests for that.

But classes in particular are tricky, because (a) you have to look up
members the right way or ``classmethod`` and ``staticmethod`` hide
from you, and (b) you have to integrate correctly with autodoc for
``:members:`` to automatically use your custom directives.

.. note::

   .. autoclass:: ExampleClass
      :noindex:
      :members:
      :undoc-members:

   .. code-block:: none

      <em class="property">abstractmethod </em><code class="(sig-name )?descname">abstractmethod_</code>

   .. code-block:: none

      <em class="property">abstractmethod classmethod </em><code class="(sig-name )?descname">classabstract</code>

   .. code-block:: none

      <em class="property">classmethod </em><code class="(sig-name )?descname">classmethod_</code>

   .. code-block:: none

      <em class="property">await </em><code class="(sig-name )?descname">asyncmethod</code>


Autodoc + order by source:

.. autoclass:: ExampleClassForOrder
   :members:
   :undoc-members:

Autodoc + inherited methods:

.. note::

   .. autoclass:: ExampleInheritedSubclass
      :noindex:
      :members:
      :undoc-members:
      :inherited-members:

   .. code-block:: none

      <em class="property">await </em><code class="(sig-name )?descname">c_asyncmethod</code>

   .. code-block:: none

      <em class="property">await </em><code class="(sig-name )?descname">d_asyncmethod</code>

.. warning::

   .. autoclass:: ExampleInheritedSubclass
      :noindex:
      :members:
      :undoc-members:
      :inherited-members:

   .. code-block:: none

      <em class="property">await </em><code class="(sig-name )?descname">a_syncmethod</code>

   .. code-block:: none

      <em class="property">await </em><code class="(sig-name )?descname">b_syncmethod</code>


Autodoc + explicit options:

.. note::

   .. autofunction:: basic
      :noindex:
      :for:
      :async:

   .. code-block:: none

      <em class="property">for ... in await </em><code class="(sig-prename )?descclassname">autodoc_examples.</code><code class="(sig-name )?descname">basic</code>

Overriding sniffed ``:for:`` with ``:for: arg``:

.. note::

   .. autofunction:: gen
      :noindex:

   .. code-block:: none

      <em class="property">for ... in </em><code class="(sig-prename )?descclassname">autodoc_examples.</code><code class="(sig-name )?descname">gen</code>

.. note::

   .. autofunction:: gen
      :noindex:
      :for: arg

   .. code-block:: none

      <em class="property">for arg in </em><code class="(sig-prename )?descclassname">autodoc_examples.</code><code class="(sig-name )?descname">gen</code>

Testing ``:no-auto-options:``:

.. note::

   .. autofunction:: gen
      :noindex:
      :no-auto-options:

   .. code-block:: none

      <dt>
      <code class="(sig-prename )?descclassname">autodoc_examples.</code><code class="(sig-name )?descname">gen</code>

.. warning::

   .. autofunction:: gen
      :noindex:
      :no-auto-options:

   .. code-block:: none

      for

.. note::

   .. autofunction:: gen
      :noindex:
      :no-auto-options:
      :for:

   .. code-block:: none

      <em class="property">for ... in </em><code class="(sig-prename )?descclassname">autodoc_examples.</code><code class="(sig-name )?descname">gen</code>

.. note::

   .. autofunction:: gen
      :noindex:
      :no-auto-options:
      :async:

   .. code-block:: none

      <em class="property">await </em><code class="(sig-prename )?descclassname">autodoc_examples.</code><code class="(sig-name )?descname">gen</code>


Autodoc + Autosummary
---------------------

See: https://github.com/python-trio/sphinxcontrib-trio/issues/8

Previously the presence of this code in the file (when combined with
``autosummary_generate = True`` in ``conf.py``) would cause all the
*other* ``autofunction`` tests to fail...

.. autosummary::
   :toctree:

   autosummary_me
