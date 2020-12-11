.DEFAULT_GOAL := new
day ?= $(shell date "+%-d")

new:
ifneq (,$(wildcard ./src/task$(day).py))
	# Day exists
else
	sed -e 's/{{ day }}/${day}/g' task.tpl > "src/task$(day).py"
	sed -e 's/{{ day }}/${day}/g' test_task.tpl > "src/test_task$(day).py"
	touch "resources/task$(day).input"
endif

run:
	python3 -m "src.task${day}"

test:
	python -m unittest -v "src.test_task${day}"
