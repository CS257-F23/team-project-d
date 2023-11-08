DROP TABLE IF EXISTS "reproductiveHealthAndDemographicData";
DROP TABLE IF EXISTS test;
CREATE TABLE "reproductiveHealthAndDemographicData" (
  userID int,
  states text,
  region text,
  homeownership text,
  marriage text,
  employ1 text,
  education text,
  race text,
  poliParty text,
  poliView text,
  religion text,
  insurance text,
  birthcontrol_use text,
  birthcontrol_access text
);