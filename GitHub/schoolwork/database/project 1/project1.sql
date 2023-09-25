CREATE SCHEMA project1_Hoyoung;
USE project1_Hoyoung;

CREATE TABLE brand
(
    brandId INT PRIMARY KEY,
    brandName VARCHAR(100)
);

CREATE TABLE color
(
    colorId INT PRIMARY KEY,
    colorName VARCHAR(100)
);

CREATE TABLE formfactor
(
    formId INT PRIMARY KEY,
	formName VARCHAR(100)
);

CREATE TABLE computerCase
(
    computerCaseId INT PRIMARY KEY,
    brandId INT,
    colorId INT,
	num_120fans INT,
    caseName VARCHAR(100),
    FOREIGN KEY (brandId) REFERENCES brand(brandId),
	FOREIGN KEY (colorId) REFERENCES color(colorId)
);

CREATE TABLE powersupply
(
    powersupplyId INT PRIMARY KEY,
    powersupplyName VARCHAR(100),
	wattageOut INT,
    brandId INT,
    colorId INT,
    FOREIGN KEY (brandId) REFERENCES brand(brandId),
	FOREIGN KEY (colorId) REFERENCES color(colorId)
);

CREATE TABLE cpu_socket_type
(
    TypeId INT PRIMARY KEY,
    TypeName VARCHAR(100),
    brandId INT,
    FOREIGN KEY (brandId) REFERENCES brand(brandId)
);

CREATE TABLE central_Processing_Unit
(
    cpuId INT PRIMARY KEY,
    cpuName VARCHAR(100),
    brandId INT,
    wattageIn INT,
    FOREIGN KEY (brandId) REFERENCES brand(brandId)
);

CREATE TABLE motherboard
(
    motherboardId int PRIMARY KEY,
    motherboardName VARCHAR(100),
    brandId INT,
    colorId INT,
    FOREIGN KEY (brandId) REFERENCES brand(brandId),
	FOREIGN KEY (colorId) REFERENCES color(colorId)
);

CREATE TABLE gaphics_Processing_Unit
(
    gpuId INT PRIMARY KEY,
    gpuName VARCHAR(100),
    brandId INT,
    colorId INT,
    wattageIn INT,
    FOREIGN KEY (brandId) REFERENCES brand(brandId),
	FOREIGN KEY (colorId) REFERENCES color(colorId)
);

CREATE TABLE ram_Speed_Type
(
    TypeId INT PRIMARY KEY,
    TypeName VARCHAR(20)
);

CREATE TABLE ram
(
    ramId INT PRIMARY KEY,
    ramName VARCHAR(100),
    brandId INT,
    TypeId INT,
    FOREIGN KEY (brandId) REFERENCES brand(brandId),
    FOREIGN KEY (TypeId) REFERENCES ram_Speed_Type(TypeId)
);

CREATE TABLE hard_disk
(
    hard_diskId INT PRIMARY KEY,
    hard_diskName VARCHAR(100),
    brandId INT,
    FOREIGN KEY (brandId) REFERENCES brand(brandId)
);

CREATE TABLE caseFormFactor_junction
(
    computerCaseId INT,
    formId INT,
    PRIMARY KEY (computerCaseId, formId),
    FOREIGN KEY (computerCaseId) REFERENCES computerCase(computerCaseId),
    FOREIGN KEY (formId) REFERENCES formfactor(formId)
);

CREATE TABLE ram_Speed_junction
(
    TypeId INT,
    cpuId INT,
    PRIMARY KEY (TypeId, cpuId),
    FOREIGN KEY (cpuId) REFERENCES central_Processing_Unit(cpuId),
    FOREIGN KEY (TypeId) REFERENCES ram_Speed_Type(TypeId)
);

CREATE TABLE ram_motherboard_junction
(
    TypeId INT, 
    motherboardId INT,
    PRIMARY KEY (TypeId, motherboardId),
    FOREIGN KEY (motherboardId) REFERENCES motherboard(motherboardId),
    FOREIGN KEY (TypeId) REFERENCES ram_Speed_Type(TypeId)
);

CREATE TABLE cpu_socket_type_junction
(
    TypeId INT, 
    motherboardId INT,
    PRIMARY KEY (TypeId, motherboardId),
    FOREIGN KEY (motherboardId) REFERENCES motherboard(motherboardId),
    FOREIGN KEY (TypeId) REFERENCES cpu_socket_type(TypeId)
);

INSERT INTO project1_hoyoung.color (colorId, colorName) 
VALUES 
    ('1', 'black'),
    ('2', 'white');
INSERT INTO brand (brandId, brandName) 
VALUES 
    (1,'Intel'),
    (2,'AMD'),
    (3,'CORSAIR'),
    (4,'GIGABYTE'),
    (5,'EVGA'),
    (6,'MSI'),
    (7,'SAMSUNG'),
    (8,'ZOTAC'),
    (9,'Fractal Design'),
    (10, 'Thermaltake'),
    (11, 'ASUS'),
    (12, 'Seasonic'),
    (13, 'T-Force'),
    (14, 'G.Skill');
INSERT INTO project1_hoyoung.formfactor (formId, formName) 
VALUES 
    (1, 'ATX'),
    (2, 'Micro ATX'),
    (3, 'Mini ITX'),
    (4, 'E-ATX');

INSERT INTO project1_hoyoung.ram_Speed_Type (`TypeId`, `TypeName`) 
VALUES 
    ('1', 'DDR4-3200'),
    ('2', 'DDR4-3600'),
    ('3', 'DDR5-6400'),
    ('4', 'DDR5-5600');
INSERT INTO project1_hoyoung.cpu_socket_type (TypeId, TypeName, brandId) 
VALUES 
    (1, 'LGA 1700', 1),
    (2, 'Socket AM5', 2),
    (3, 'Socket AM4', 2),
    (4, 'LGA 1200', 1);
INSERT INTO project1_hoyoung.central_processing_unit (cpuId, cpuName, brandId, wattageIn)
VALUES 
    (1, 'Ryzen 5 5600', 2, 65),
    (2, 'i5-12400F', 1, 65),
    (3, 'i7-12700k', 1, 125),
    (4, 'Ryzen 7 5800x', 2, 105),
    (5, 'i9-13900k', 1, 125),
    (6, 'Ryzen 9 7950X', 2, 170);
INSERT INTO project1_hoyoung.powersupply (powersupplyId, powersupplyName, wattageOut, brandId, colorId) 
VALUES 
    ('1', 'FOCUS GX-750', '750', '12', '1'),
    ('2', '220-G5-0650-X1', '650', '5', '1'),
    ('3', 'CP-9020199-NA', '750', '3', '1'),
    ('4', 'CP-9020200-NA', '850', '3', '1'),
    ('5', 'CP-9020201-NA', '1000 ', '3', '1');
INSERT INTO project1_hoyoung.computercase (computerCaseId, brandId, colorId, num_120fans, caseName)
VALUES 
    (1, 3, 1, 6, '4000D Airflow'),
    (2, 3, 2, 6, '4000D Airflow'),
    (3, 3, 1, 10, '5000D Airflow'),
    (4, 9, 2, 7, 'Meshify C'),
    (5, 10, 1, 11, 'The Tower 500'),
    (6, 3, 1, 10, '5000D RGB AIRFLOW');
INSERT INTO project1_hoyoung.gaphics_processing_unit (gpuId, gpuName, brandId, colorId, wattageIn)
VALUES 
    (1, 'GeForce RTX 3060', 8, 1, 600),
    (2, 'GeForce RTX 3060', 4, 1, 550),
    (3, 'GeForce RTX 3070', 6, 1, 650),
    (4, 'GeForce RTX 3070', 4, 1, 650),
    (5, 'GeForce RTX 4090', 4, 1, 1000),
    (6, 'GeForce RTX 4090', 11, 1, 1000);
INSERT INTO project1_hoyoung.hard_disk (hard_diskId, hard_diskName, brandId)
VALUES 
    (1, '970 EVO PLUS', 7),
    (2, 'SPATIUM M371 NVMe M.2 1TB', 6),
    (3, '980 PRO', 7);
INSERT INTO project1_hoyoung.motherboard (motherboardId, motherboardName, brandId, colorId)
VALUES 
    (1, 'PRO B550M-VC WIFI', 6, 1),
    (2, 'PRO Z690-A DDR4', 6, 1),
    (3, 'TUF GAMING X570-PLUS (Wi-Fi)', 11, 1),
    (4, 'Z790 AORUS ELITE AX', 4, 1),
    (5, 'PROART X670E-CREATOR WIFI', 11, 1);
INSERT INTO project1_hoyoung.ram (ramId, ramName, brandId, TypeId)
VALUES 
    (1, 'TLZGD416G3200HC16CDC01', 13, 1),
    (2, 'CMW16GX4M2C3200C16', 3, 1),
    (3, 'CMK32GX4M2D3600C18', 3, 2),
    (4, 'F4-3200C16D-32GVK', 14, 1),
    (5, 'F5-6400J3239G16GX2-TZ5RK', 14, 3),
    (6, 'CMK32GX5M2B5600C36', 3, 4);
INSERT INTO project1_hoyoung.caseformfactor_junction (computerCaseId, formId)
VALUES 
    (1, 1),
    (1, 2),
    (1, 3),
    (1, 4),
    (2, 1),
    (2, 2),
    (2, 3),
    (2, 4),
    (3, 1),
    (3, 2),
    (3, 3),
    (3, 4),
    (4, 1),
    (4, 2),
    (4, 3),
    (5, 1),
    (5, 2),
    (5, 3),
    (5, 4),
    (6, 1),
    (6, 2),
    (6, 3),
    (6, 4);
INSERT INTO project1_hoyoung.cpu_socket_type_junction (TypeId, motherboardId)
VALUES 
    (3, 1),
    (1, 2),
    (3, 3),
    (1, 4),
    (2, 5);
INSERT INTO project1_hoyoung.ram_motherboard_junction (TypeId, motherboardId)
VALUES 
    (1, 1),
    (2, 1),
    (1, 2),
    (1, 3),
    (2, 3),
    (3, 4),
    (4, 4),
    (3, 5),
    (4, 5);
INSERT INTO project1_hoyoung.ram_speed_junction (TypeId, cpuId)
VALUES 
    (1, 1),
    (1, 2),
    (1, 3),
    (1, 4),
    (1, 5),
    (4, 5),
    (4, 6);

-- find all e-ATX
SELECT 
    cc.caseName
FROM 
    computerCase cc
JOIN 
    caseFormFactor_junction cfj ON cc.computerCaseId = cfj.computerCaseId
JOIN 
    formfactor ff ON cfj.formId = ff.formId
WHERE 
    ff.formName = 'e-ATX';

-- find motherboards with DDR4-3200 capability and cpu that matches the motherboard and the capability
SELECT 
    r.ramName, 
    mb.motherboardName, 
    cpu.cpuName
FROM 
    ram r
JOIN 
    ram_motherboard_junction rmj ON r.TypeId = rmj.TypeId
JOIN 
    motherboard mb ON mb.motherboardId = rmj.motherboardId
JOIN 
    cpu_socket_type_junction cstj ON mb.motherboardId = cstj.motherboardId
JOIN 
    central_Processing_Unit cpu ON cpu.cpuId = cstj.TypeId
JOIN 
    ram_speed_junction rsj ON r.TypeId = rsj.TypeId
WHERE 
    r.TypeId = (SELECT TypeId FROM ram_Speed_Type WHERE TypeName = 'DDR4-3200')
    AND cpu.cpuId = rsj.cpuId;

-- find all white cases
SELECT 
    'Computer Case' AS ComponentType, cc.caseName AS ComponentName
FROM 
    computerCase cc
JOIN
    color c ON cc.colorId = c.colorId
WHERE 
    c.colorName = 'white';

-- all power supply that can be ran with powersupplyId 2
SELECT 
    gpu.gpuName
FROM 
    gaphics_Processing_Unit gpu
WHERE 
    gpu.wattageIn <= (
SELECT 
    ps.wattageOut
FROM 
    powersupply ps
WHERE 
    ps.powersupplyId = 2
);

-- find all components by corsair
SELECT 
    'Computer Case' AS ComponentType, cc.caseName AS ComponentName
FROM 
    computerCase cc
JOIN 
    brand b ON cc.brandId = b.brandId
WHERE 
    b.brandName = 'CORSAIR'

UNION ALL

SELECT 
    'Power Supply' AS ComponentType, ps.powersupplyName AS ComponentName
FROM 
    powersupply ps
JOIN 
    brand b ON ps.brandId = b.brandId
WHERE 
    b.brandName = 'CORSAIR'

UNION ALL

SELECT 
    'Central Processing Unit' AS ComponentType, cpu.cpuName AS ComponentName
FROM 
    central_Processing_Unit cpu
JOIN 
    brand b ON cpu.brandId = b.brandId
WHERE 
    b.brandName = 'CORSAIR'

UNION ALL

SELECT 
    'Graphics Processing Unit' AS ComponentType, gpu.gpuName AS ComponentName
FROM 
    gaphics_Processing_Unit gpu
JOIN 
    brand b ON gpu.brandId = b.brandId
WHERE 
    b.brandName = 'CORSAIR'

UNION ALL

SELECT 
    'RAM' AS ComponentType, ram.ramName AS ComponentName
FROM 
    ram ram
JOIN 
    brand b ON ram.brandId = b.brandId
WHERE 
    b.brandName = 'CORSAIR';