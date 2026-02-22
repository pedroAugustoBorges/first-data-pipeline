ALTER TABLE members DROP CONSTRAINT IF EXISTS motivation_member_uk;
ALTER TABLE members ADD CONSTRAINT motivation_member_uk UNIQUE (motivation_member)