.DEFAULT_GOAL := new

month := $(shell date "+%-0m")
ifeq ($(month), 12)
	day ?= $(shell date "+%-d")
else
	day ?= 1
endif
d = $(shell printf "%02d" ${day})

new:
ifneq (,$(wildcard ./src/task${d}.py))
	# Day exists
else
	sed -e 's/{{ day }}/${d}/g' task.tpl > "src/task${d}.py"
	sed -e 's/{{ day }}/${d}/g' test_task.tpl > "tests/test_task${d}.py"
	touch "resources/task${d}.input"
endif

run:
	time python3 -m "src.task${d}"

test:
	python -m unittest -v "tests.test_task${d}"
