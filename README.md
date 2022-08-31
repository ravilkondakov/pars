This parser provide you save nested title and url from
another sites in database.

in pars/parser.py add url witch site you want to save nested titles and urls


for running test use command 
- docker-compose run --rm --entrypoint "python -m unittest pars/tests.py" app

for running parser use command
- docker-compose run --rm app python pars/parser.py

