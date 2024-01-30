# Guide to Buiding and Publishing PyPi Packages

## Onboarding Project to Build PyPi Module

- `make check`
- `make setup`
- local dev, edit, and build
- `make build`
- `make push-test` to TEST
- `make push` to PROD

## Local Development

Install the package locally editable
- `pip uninstall slowblood -y`
- `pip install -e ./pypi/src/slowblood`

## File Structure

> example `slowblood` module

```
├── pypi
│   ├── README.md
│   ├── dist (ignored, from build for publishing)
│   │   ├── slowblood-0.0.8-py3-none-any.whl
│   │   └── slowblood-0.0.8.tar.gz
│   ├── pyproject.toml
│   ├── setup.cfg
│   ├── src
│   │   ├── slowblood
│   │   │   ├── __init__.py
│   │   │   ├── lib_dataset.py
│   │   │   ├── lib_llm_inference.py
│   │   │   ├── lib_model.py
│   │   │   ├── lib_pdf.py
│   │   │   ├── lib_prompts.py
│   │   │   ├── lib_runpod.py
│   │   │   ├── lib_settings.py
│   │   │   ├── lib_tokenizer.py
│   │   │   └── lib_toolkit.py
│   │   └── slowblood.egg-info (ignored, for build)
│   │       ├── PKG-INFO
│   │       ├── SOURCES.txt
│   │       ├── dependency_links.txt
│   │       ├── requires.txt
│   │       └── top_level.txt
│   └── tests

```

## Test Server

Push to Test Repository
- `python -m twine upload --repository testpypi dist/*` 
- username: `__token__` and your token as password
- Create a seperate account at `test.pypi.org` and tokens
- Sample url: `https://test.pypi.org/project/slowblood/0.0.8/`

Download like:
- `pip install -i https://test.pypi.org/simple/ slowblood`

## References
- https://www.youtube.com/watch?v=WGsMydFFPMk
- https://www.youtube.com/watch?v=Kz6IlDCyOUY