.DEFAULT_GOAL := new
day ?= 1

new:
ifneq (,$(wildcard ./task$(day).*))
	# Day exists
else
	sed -e 's/{{ day }}/${day}/g' task.tpl > "task$(day).py"
	sed -e 's/{{ day }}/${day}/g' test_task.tpl > "test_task$(day).py"
	touch "task$(day).input"
endif

run:
	python3 -m "task${day}"

test:
	python -m unittest -v "test_task${day}"
