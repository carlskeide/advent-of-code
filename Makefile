.DEFAULT_GOAL := new

year := $(shell date "+%-0Y")
month := $(shell date "+%-0m")
ifeq ($(month), 12)
	day ?= $(shell date "+%-d")
else
	day ?= 1
endif
d = $(shell printf "%02d" ${day})

new:
ifneq (,$(wildcard ./${year}/task${d}.py))
	# Day exists
else
	sed -e 's/{{ day }}/${d}/g' task.tpl > "${year}/task${d}.py"
	sed -e 's/{{ day }}/${d}/g' test_task.tpl > "${year}/task${d}_test.py"
	touch "resources/task${d}.input"
endif

run:
	time python3 -m "${year}.task${d}"

test:
	python -m unittest -v "${year}.task${d}_test"
