-- Creating a Multicolumn index
CREATE INDEX  last_name_first_name_idx
ON customers(last_name, first_name);