#####
Usage
#####



You must have Git installed.

Install this extension:

.. code-block:: shell

    pip install sphinxcontrib-git-context

Enable this extension in the configuration file ``conf.py``:

.. code-block:: python

    extensions = [
        ...
        'sphinxcontrib.git_context'
    ]

If you wish, override the defaults in the configuration file ``conf.py``:

.. code-block:: python

    def custom_git_context_setup(config):
        # config: sphinx.config.Config
        # Git metadata are stored in the global configuration object:
        git_context = config['git_context']
        # here are the available values:
        generated_at = git_context['generated_at']
        commit_date = git_context['commit_date']
        commit_tags = git_context['commit_tags']
        commit_hash = git_context['commit_hash']
        dirty = git_context['dirty']
        # use these values to set the version and the release variable:
        config['version'] = 'use the available values'
        config['release'] = 'use the available values'
    # give the custom method to the plugin, overriding the default one
    git_context_setup = custom_git_context_setup
