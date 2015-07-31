PYTHON := $(shell which python2.7)
MAIN := $(CURDIR)/infix.py

.PHONY: test

test:
	$(PYTHON) $(MAIN)
