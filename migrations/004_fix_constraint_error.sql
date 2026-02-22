ALTER TABLE members
DROP CONSTRAINT motivation_member_uk;

ALTER TABLE members DROP CONSTRAINT IF EXISTS discord_id_uk;
ALTER TABLE members ADD CONSTRAINT discord_id_uk UNIQUE (discord_id)