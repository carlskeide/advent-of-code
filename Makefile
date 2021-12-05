.DEFAULT_GOAL := new

year := $(shell date "+%-0Y")
month := $(shell date "+%-0m")
ifeq ($(month), 12)
	day ?= $(shell date "+%-d")
else
	day ?= 1
endif
f = $(shell printf "task%02d" ${day})

new:
ifneq (,$(wildcard ./${year}/${f}.py))
	# Day exists
else
	sed -e 's/{{ day }}/${day}/g' task.tpl > "${year}/${f}.py"
	sed -e 's/{{ task }}/${f}/g' test_task.tpl > "${year}/${f}_test.py"
	touch "${year}/${f}.input"
endif

run:
	/usr/bin/time -f'Time: %E' -- python3 -m "${year}.${f}"

test:
	python -m unittest -v "${year}.${f}_test"
