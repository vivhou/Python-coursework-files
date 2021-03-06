#! /user/bin/python# -*- coding: utf8 -*-
import sqlite3 as lite
import sys

con = lite.connect('db/private_universities2.db')

menu =(
('Alaska Pacific University',100,15917),
('Alderson Broaddus University',100,15807),
('Alice Lloyd College',100,8352),
('Alliant International University-San Diego',88,11988),
('American Jewish University',86,12107),
('American Musical and Dramatic Academy',100,9676),
('American University',71,22854),
('Amherst College',57,46857),
('Andrews University',98,11516),
('Antioch College',100,30339),
('Art Academy of Cincinnati',100,16765),
('Babson College',49,33057),
('Bacone College',82,5246),
('Bais Medrash Toras Chesed',68,7571),
('Bard College',67,37297),
('Barnard College',47,39509),
('Barry University',97,19316),
('Barton College',99,17841),
('Bates College',48,38938),
('Bellin College',49,1474),
('Bentley University',68,25120),
('Berea College',100,29880),
('Berklee College of Music',51,16629),
('Bethel College-North Newton',100,16369),
('Boston College',42,34327),
('Boston University',52,28848),
('Bowdoin College',48,37611),
('Brandeis University',57,34635),
('Brescia University',91,16954),
('Brevard College',100,15892),
('Bridgewater College',100,23086),
('Brigham Young University-Hawaii',74,4297),
('Brigham Young University-Provo',50,4443),
('Brown University',46,39267),
('Bryan College-Dayton',96,14941),
('Bryn Mawr College',73,27475),
('Bucknell University',56,27933),
('California Institute of Technology',55,31845),
('California Institute of the Arts',69,14694),
('Calumet College of Saint Joseph',88,9075),
('Carleton College',69,28384),
('Carlos Albizu University-Miami',67,5848),
('Carnegie Mellon University',53,28322),
('Case Western Reserve University',84,28418),
('Catawba College',100,19442),
('Central Christian College of Kansas',95,11017),
('Central Christian College of the Bible',100,12471),
('Chapman University',84,23663),
('Christian Brothers University',100,22115),
('Claflin University',91,12460),
('Claremont McKenna College',45,38028),
('Cleveland Institute of Music',100,27152),
('Colby College',42,40633),
('Colgate University',42,38401),
('College for Creative Studies',99,13965),
('College of the Holy Cross',52,31581),
('College of the Ozarks',100,12664),
('Colorado College',48,33259),
('Columbia International University',95,13124),
('Columbia University in the City of New York',47,43306),
('Connecticut College',54,36532),
('Cooper Union for the Advancement of Science and Art',100,40544),
('Corban University',100,16356),
('Cornell University',50,33064),
('Crown College',91,13110),
('Cumberland University',100,15619),
('Curtis Institute of Music',55,12485),
('Dallas Baptist University',92,10230),
('Dallas Christian College',98,10349),
('Dartmouth College',47,42002),
('Davidson College',60,35001),
('Davis College',100,8188),
('Dickinson College',70,26620),
('Dillard University',97,11726),
('Duke University',45,39984),
('Emerson College',59,19066),
('Emmanuel College',100,11316),
('Emmaus Bible College',100,6938),
('Emory University',52,31705),
('Finlandia University',93,10083),
('Flagler College-St Augustine',88,7182),
('Florida Memorial University',87,8991),
('Florida Southern College',99,17000),
('Fordham University',89,24219),
('Franklin and Marshall College',51,37791),
('Franklin W Olin College of Engineering',100,31977),
('George Washington University',67,28562),
('Georgetown University',42,36393),
('Gettysburg College',66,24977),
('Grace University',100,13940),
('Graceland University-Lamoni',100,17411),
('Grinnell College',93,31458),
('Hamilton College',53,37198),
('Hampden-Sydney College',98,22435),
('Hampton University',76,11226),
('Harvard University',56,44855),
('Harvey Mudd College',70,30723),
('Haverford College',50,39489),
('Hiwassee College',91,9666),
('Hobart William Smith Colleges',85,23968),
('Hope International University',99,15652),
('Houston Baptist University',100,17352),
('Howard University',82,19306),
('Inter American University of Puerto Rico-Barranquitas',100,5467),
('Inter American University of Puerto Rico-Metro',89,5398),
('Iowa Wesleyan College',100,18057),
('Johns Hopkins University',48,36274),
('Johnson C Smith University',91,12903),
('Johnson University Florida',82,6567),
('Keiser University-Ft Lauderdale',95,6521),
('Kentucky Christian University',100,10437),
('Kenyon College',44,33226),
('La Sierra University',99,16671),
('Lafayette College',53,32731),
('Lane College',94,7307),
('Lehigh University',50,29161),
('LeTourneau University',97,16954),
('Liberty University',93,8891),
('Lincoln Christian University',94,8644),
('Macalester College',75,29479),
('Maharishi University of Management',100,19846),
('Manhattan School of Music',56,22061),
('Maria College of Albany',62,6940),
('Marist College',88,13673),
('Marygrove College',96,14553),
('Massachusetts Institute of Technology',56,36808),
('Memphis College of Art',99,19977),
('Menlo College',96,21349),
('Methodist College',100,6320),
('Mid-Atlantic Christian University',100,8602),
('Middlebury College',45,38567),
('Missouri Valley College',100,13123),
('Montreat College',99,17205),
('Mount Mary University',100,21184),
('New York School of Interior Design',52,12255),
('New York University',53,26447),
('Northeastern University',69,27442),
('Northwestern University',54,34363),
('Northwood University-Florida',95,15075),
('Notre Dame of Maryland University',100,24515),
('Nova Southeastern University',97,17264),
('Oakwood University',91,9154),
('Oberlin College',86,23211),
('Occidental College',69,30617),
('Ohio Dominican University',100,21129),
('Ohio Valley University',100,10318),
('Our Lady of the Lake University',99,16854),
('Pacific Union College',100,16826),
('Paine College',89,8559),
('Pennsylvania College of Art and Design',84,5590),
('Pennsylvania College of Health Sciences',58,4046),
('Pepperdine University',79,33527),
('Pfeiffer University',83,18145),
('Piedmont International University',84,6206),
('Pitzer College',35,35334),
('Pomona College',58,40525),
('Pontifical Catholic University of Puerto Rico-Arecibo',93,5212),
('Princeton University',62,38515),
('Providence Christian College',100,17403),
('Reed College',49,40831),
('Rensselaer Polytechnic Institute',92,25446),
('Rhode Island School of Design',38,26267),
('Rice University',58,33779),
('Robert Morris University Illinois',97,12644),
('Rochester College',97,11109),
('Rust College',99,5489),
('Saint Xavier University',100,19614),
('San Francisco Conservatory of Music',100,22054),
('Santa Clara University',71,22507),
('Scripps College',58,26333),
('Shimer College',100,10305),
('Shorter University-College of Adult & Professional Programs',100,3997),
('Silver Lake College of the Holy Family',100,15389),
('Skidmore College',45,36584),
('Smith College',63,34548),
('Soka University of America',100,28441),
('Southeastern University',90,12180),
('Southern Virginia University',94,8189),
('Southwestern Adventist University',99,9913),
('Southwestern Assemblies of God University',95,8284),
('Southwestern University',100,22418),
('Spalding University',99,14136),
('St Lawrence University',96,28612),
("St Vincent's College",100,8171),
('Stanford University',51,42359),
('Sterling College',100,14212),
('Stevens Institute of Technology',97,27881),
('Summit Christian College',100,1413),
('Swarthmore College',52,38114),
('Texas Christian University',65,19465),
('Texas Wesleyan University',91,10411),
('The Boston Conservatory',74,17474),
('The College of New Rochelle',99,11906),
('The Juilliard School',78,26627),
('The New England Conservatory of Music',97,14784),
('Toccoa Falls College',98,13053),
('Tougaloo College',64,9798),
('Touro College',83,8684),
('Touro University Worldwide',75,9220),
('Trinity Bible College',88,9256),
('Trinity College',43,37190),
('Trinity University',94,20756),
('Tufts University',38,34897),
('Tulane University of Louisiana',70,28249),
('Tuskegee University',78,4439),
('Union College',75,26233),
('Universidad Central Del Caribe',83,5193),
('Universidad del Sagrado Corazon',80,5639),
('University of Chicago',63,30636),
('University of La Verne',96,23574),
('University of Miami',76,26587),
('University of Mount Olive',98,14590),
('University of Notre Dame',57,33092),
('University of Pennsylvania',50,39106),
('University of Richmond',56,33527),
('University of Rochester',86,28344),
('University of Saint Mary',99,15473),
('University of San Diego',79,25200),
('University of Southern California',59,30912),
('University of Tulsa',88,21679),
('Vanderbilt University',65,38939),
('Vassar College',57,41659),
('Villanova University',55,25750),
('Virginia Union University',85,8520),
('Visible Music College',55,3880),
('Wake Forest University',40,34312),
('Warner University',99,13797),
('Washington & Jefferson College',100,23558),
('Washington Adventist University',93,12303),
('Washington and Lee University',54,37875),
('Washington University in St Louis',51,30381),
('Watkins College of Art Design & Film',85,4947),
('Webb Institute',100,43544),
('Wellesley College',60,37876),
('Wesleyan University',38,38693),
('Whitman College',78,22812),
('Wilberforce University',100,10434),
('Williams College',49,41535),
('Wilson College',97,20081),
('Worcester Polytechnic Institute',98,20360),
('Yale University',50,42303),
("Yeshiva D'monsey Rabbinical College",100,8988),
('York College',97,8242),
('York College Pennsylvania',98,7032)

)
with con: 
	cur = con.cursor()
	cur.execute("DROP TABLE IF EXISTS Private2")
	cur.execute("CREATE TABLE Private2(id TEXT,  percent_awarded INT,  average_award INT)")

	cur.executemany("INSERT INTO Private2 VALUES(?,  ?,  ?)",  menu)