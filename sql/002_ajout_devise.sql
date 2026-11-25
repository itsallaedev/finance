USE finance;
ALTER TABLE societe
ADD COLUMN devise VARCHAR(3) NOT NULL DEFAULT 'EUR';

-- Vérification
SELECT nom, devise FROM societe;