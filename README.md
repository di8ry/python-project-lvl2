## Generate diff:
[![Actions Status](https://github.com/di8ry/python-project-lvl2/workflows/hexlet-check/badge.svg)](https://github.com/di8ry/python-project-lvl2/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/8eb1e5f1c890cf752b2e/maintainability)](https://codeclimate.com/github/di8ry/python-project-lvl2/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/8eb1e5f1c890cf752b2e/test_coverage)](https://codeclimate.com/github/di8ry/python-project-lvl2/test_coverage)


### As CLI tool
Gendiff is a CLI utility for finding differences between configuration files.

                        
### Comparing flat JSON files

gendiff simple_before.json simple_after.json

[![asciicast](https://asciinema.org/a/GRPXtfTjY4YriTBxbJ8cKKsrK.svg)](https://asciinema.org/a/GRPXtfTjY4YriTBxbJ8cKKsrK)

## Comparing files with nested structures

gendiff hard_before.json hard_after.json

[![asciicast](https://asciinema.org/a/k9MSkXjE1Mgc5UpNtaQMnDcVT.svg)](https://asciinema.org/a/k9MSkXjE1Mgc5UpNtaQMnDcVT)

## Plain text format for output

gendiff -f plain hard_before.json hard_after.json

[![asciicast](https://asciinema.org/a/VWpw8eZofCM6l6fl74LWfCHMh.svg)](https://asciinema.org/a/VWpw8eZofCM6l6fl74LWfCHMh)
