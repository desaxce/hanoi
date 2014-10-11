all: hanoi.py
	python $^

.PHONY: clean

clean:
	rm -rf *.pyc

