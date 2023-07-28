
-- DROP SCHEMA IF EXISTS "EJ" ;

CREATE SCHEMA IF NOT EXISTS "EJ"
    AUTHORIZATION "SvatebniDB";

-- DROP TABLE IF EXISTS "EJ"."Hoste";

CREATE TABLE IF NOT EXISTS "EJ"."Hoste"
(
    "IdHost" integer NOT NULL DEFAULT nextval('"EJ"."Hoste_IdHost_seq"'::regclass),
    "Jmeno" text COLLATE pg_catalog."default",
    "Prijmeni" text COLLATE pg_catalog."default",
    "Telefon" text COLLATE pg_catalog."default",
    "Email" text COLLATE pg_catalog."default",
    "Intolerance" text COLLATE pg_catalog."default",
    "Vegetarian" text COLLATE pg_catalog."default",
    "Alkohol" text COLLATE pg_catalog."default",
    "Nocovani" text COLLATE pg_catalog."default",
    "Tipy" text COLLATE pg_catalog."default",
    CONSTRAINT "Hoste_pkey" PRIMARY KEY ("IdHost")
)


