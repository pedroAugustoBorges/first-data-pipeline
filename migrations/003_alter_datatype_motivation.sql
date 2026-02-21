ALTER TABLE members if NOT EXISTS
ADD CONSTRAINT motivation_member_uk UNIQUE (motivation_member)