# geta, for when you need to "get a" random thing
A Python CLI app to get a random instance of a _thing_. It's starting out with simply providing random names, but I like the idea of the `geta` being able to get many more _things_.

## Usage

### `geta name`

`geta name` uses the [names package](https://pypi.org/project/names/) to generate random first, last, and full names derived from 1990 US census data.

`geta name` defaults to providing a full name but you can specify first, last, or full.

```
✘ python3 geta/main.py name
Sabrina Fusco

✘ python3 geta/main.py name --full
Kenneth Halligan

✘ python3 geta/main.py name --first
Valentina

✘ python3 geta/main.py name --first
Patrica

✘ python3 geta/main.py name --last
Monzo

✘ python3 geta/main.py name --last
Walker
```
