# Groq OpenAPI specification

There is nothing wrong with the online documentation for the Groq API, nor is
there anything wrong with their Python and JavaScript libraries.

I decided to create a Swagger [OpenAPI specification](https://swagger.io/specification/)
according to what I see on Groq's online documentation.

The openapi.yaml file is linted using: [yamllint](https://github.com/adrienverge/yamllint).

# Developer environment

I am using macOS 15.2 (on Apple Silicon) so some of the instructions may be
specific to this operating system.

All of the following commands in this README are assumed to be executed in the
repo root.

## Python specific

You do not need this exact version of Python, but I know of at least one
OpenAPI Python library (fastapi-code-generator) that is unable to use Python
3.13.

```shell
brew install python@3.12
```

The following is compatible with VSCode's setup.

Run once after cloning repo:

```shell
python3.12 -m venv .venv
```

Run each time you open a new terminal, initialize it with this:

```shell
source .venv/bin/activate
```

If you freshly cloned the repo, or pulled down new changes, AND after you
initialized your terminal, run this:

```shell
pip install -r requirements.txt
```

### Generating Python client

Run this from the repo root each time you make changes to the OpenAPI
specification:

```shell
.venv/bin/openapi-python-client generate \
    --meta poetry \
    --file-encoding utf-8 \
    --path openapi.yaml \
    --overwrite \
    --output-path=src/python/groq_generated_client
```

### Using the reference Groq client

Copy the example `.env` file.

```shell
cp .env.example .env
```

Using your favorite editor, change the value of `GROQ_API_KEY` to the API key
you generated from the Groq Console.

Now you should be able to run the following Python application to list the
supported models:

```shell
PYTHONPATH=$(pwd)/src/python/groq_generated_client \
    python src/python/groq_get_models.py
```
