-- Hola
-- HOla
USE hbtn_0c_0;
ALTER DATABASE hbtn_0c_0 CHARACTER SET  utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER table first_table CONVERT TO CHARACTER SET  utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE first_table MODIFY COLUMN name VARCHAR(26) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL;
