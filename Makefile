#
# Copyright (C) 2014 Carlos Jenkins <carlos@jenkins.co.cr>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

INPUTS  = $(wildcard src/*/*.rst)
NAMES   = $(basename $(notdir $(INPUTS)))
OUTPUTS = $(NAMES:%=presentations/%/index.html)
OUTDIR  = presentations
THEME   = hauntr

.PHONY : print clean presentations theme

all: print clean presentations theme

print:
	@echo "* Found presentations:"
	@echo "*     $(NAMES)"

clean:
	@echo "* Cleaning $(OUTDIR) folder ..."
	rm -rf $(OUTDIR)

presentations: $(OUTPUTS)

theme:
	@echo "* Copying and building $(THEME) theme ..."
	@mkdir -p $(OUTDIR)
	cp -r $(THEME) $(OUTDIR)
	python $(OUTDIR)/$(THEME)/minify.py

# Create dynamic rules
define presentation_tpl
$(OUTDIR)/$(1)/index.html:
	@echo "* Building src/$(1)/$(1).rst ..."
	@mkdir -p $(OUTDIR)/$(1)

	rst2s5.py \
		--syntax-highlight=short \
		--stylesheet='' \
		--theme-url=$(THEME) \
		"src/$(1)/$(1).rst" \
		"$(OUTDIR)/$(1)/index.html"

	cp -rf "src/$(1)/images" "$(OUTDIR)/$(1)/"

	ln -s "../$(THEME)" "$(OUTDIR)/$(1)/"
endef

$(foreach n, $(NAMES), \
    $(eval $(call presentation_tpl,$(n))) \
)
