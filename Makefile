.DEFAULT_GOAL := new

year := $(shell date "+%-0Y")
month := $(shell date "+%-0m")
ifeq ($(month), 12)
	day ?= $(shell date "+%-d")
else
	day ?= 1
endif
task = $(shell printf "task%02d" ${day})

new:
ifneq (,$(wildcard ./${year}/${f}.py))
	# Day exists
else
	sed -e 's/{{ year }}/${year}/g' -e 's/{{ day }}/${day}/g' ./templates/task.tpl > "./src/aoc${year}/${task}.py"
	sed -e 's/{{ task }}/${task}/g' ./templates/test_task.tpl > "./src/aoc${year}/${task}_test.py"
	touch "./data/aoc${year}/${task}.txt"
endif

run:
	/usr/bin/time -f'Time: %E' -- python3 -m "src.aoc${year}.${task}"

test:
	python -m unittest -v "src.aoc${year}.${task}_test"
