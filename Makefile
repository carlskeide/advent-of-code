.DEFAULT_GOAL := new

year := $(shell date "+%-0Y")
month := $(shell date "+%-0m")

ifeq ($(month), 12)
	day ?= $(shell date "+%-d")
else
	day ?= 1
endif

task = $(shell printf "task%02d" ${day})
session := $(shell cat .session-cookie)

new:
	mkdir -p ./src/aoc${year}
	mkdir -p ./private/aoc${year}
	touch ./private/aoc${year}/__init__.py

ifneq (,$(wildcard ./src/aoc${year}/${f}.py))
	# Day exists
else
	sed -e 's/{{ year }}/${year}/g' -e 's/{{ day }}/${day}/g' ./templates/task.tpl > "./src/aoc${year}/${task}.py"
	sed -e 's/{{ task }}/${task}/g' ./templates/test_task.tpl > "./src/aoc${year}/${task}_test.py"
endif

ifneq ($(session),)
	http https://adventofcode.com/${year}/day/${day}/input cookie:session=${session} > "./private/aoc${year}/${task}.txt"
else
	touch "./private/aoc${year}/${task}.txt"
endif

run:
	/usr/bin/time -f'Time: %E' -- python3 -m "src.aoc${year}.${task}"

test:
	python -m unittest -v "src.aoc${year}.${task}_test"

lint:
	flake8 --extend-ignore F403,F405 --max-line-length=119 ./src/aoc${year}/${task}*
	mypy ./src/aoc${year}/${task}.py
