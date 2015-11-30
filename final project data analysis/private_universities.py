#! /user/bin/python# -*- coding: utf8 -*-
import sqlite3 as lite
import sys

con = lite.connect('private_universities.db')

menu =(
	('Alaska Pacific University', -34.2),
	('Alderson Broaddus University', 0.0),
	('Alice Lloyd College', 3.4),
	('Alliant International University-San Diego', 3.4),
	('American Jewish University', 4.4),
	('American Musical and Dramatic Academy', 2.5),
	('American University', 2.9),
	('Amherst College', 4.2),
	('Andrews University', 3.1),
	('Antioch College', 12.5),
	('Art Academy of Cincinnati', 8.4),
	('Babson College', 3.7),
	('Bacone College', 0.0),
	('Bais Medrash Toras Chesed', 0.0),
	('Bard College', 4.0),
	('Barnard College', 2.8),
	('Barry University', 0.0),
	('Barton College', 5.0),
	('Bates College', 3.0),
	('Bellin College', 0.5),
	('Bentley University', 3.4),
	('Berea College', 4.7),
	('Berklee College of Music', 3.5),
	('Bethel College-North Newton', 3.0),
	('Boston College', 4.0),
	('Boston University', 3.9),
	('Bowdoin College', 3.0),
	('Brandeis University', 3.7),
	('Brescia University', 1.8),
	('Brevard College', 3.8),
	('Bridgewater College', 4.4),
	('Brigham Young University-Hawaii', 3.6),
	('Brigham Young University-Provo', 3.1),
	('Brown University', 4.0),
	('Bryan College-Dayton', 5.0),
	('Bryn Mawr College', 3.7),
	('Bucknell University', 3.4),
	('California Institute of Technology', 4.4),
	('California Institute of the Arts', 4.3),
	('Calumet College of Saint Joseph', 5.0),
	('Carleton College', 3.4),
	('Carlos Albizu University-Miami', 1.6),
	('Carnegie Mellon University', 2.9),
	('Case Western Reserve University', 3.2),
	('Catawba College', 2.0),
	('Central Christian College of Kansas', 9.5),
	('Central Christian College of the Bible', -15.2),
	('Chapman University', 4.2),
	('Christian Brothers University', 3.5),
	('Claflin University', 0.0),
	('Claremont McKenna College', 3.9),
	('Cleveland Institute of Music', 0.8),
	('Colby College', 3.5),
	('Colgate University', 3.9),
	('College for Creative Studies', 3.9),
	('College of the Holy Cross', 3.2),
	('College of the Ozarks', 1.1),
	('Colorado College', 4.9),
	('Columbia International University', 2.9),
	('Columbia University in the City of New York', 3.8),
	('Connecticut College', 3.6),
	('Cooper Union for the Advancement of Science and Art', 0.0),
	('Corban University', 4.4),
	('Cornell University', 4.3),
	('Crown College', 3.3),
	('Cumberland University', 0.0),
	('Curtis Institute of Music', 2.1),
	('Dallas Baptist University', 5.8),
	('Dallas Christian College', 5.5),
	('Dartmouth College', 2.9),
	('Davidson College', 5.9),
	('Davis College', 0.0),
	('Dickinson College', 3.5),
	('Dillard University', 1.0),
	('Duke University', 4.1),
	('Emerson College', 4.5),
	('Emmanuel College', 8.2),
	('Emmaus Bible College', 0.0),
	('Emory University', 2.3),
	('Family of Faith College', 2.5),
	('Finlandia University', 4.9),
	('Flagler College-St Augustine', 0.0),
	('Florida Memorial University', 0.0),
	('Florida Southern College', 4.9),
	('Fordham University', 3.9),
	('Franklin and Marshall College', 4.8),
	('Franklin W Olin College of Engineering', 3.4),
	('George Washington University', 3.0),
	('Georgetown University', 4.3),
	('Gettysburg College', 3.5),
	('Grace University', 5.7),
	('Graceland University-Lamoni', 5.9),
	('Grinnell College', 4.5),
	('Hamilton College', 3.8),
	('Hampden-Sydney College', 5.0),
	('Hampton University', 5.0),
	('Harvard University', 3.9),
	('Harvey Mudd College', 4.5),
	('Haverford College', 3.9),
	('Hiwassee College', 1.1),
	('Hobart William Smith Colleges', 3.8),
	('Hope International University', 4.1),
	('Houston Baptist University', 3.1),
	('Howard University', 5.7),
	('Inter American University of Puerto Rico-Barranquitas', 9.1),
	('Inter American University of Puerto Rico-Metro', 4.3),
	('Iowa Wesleyan College', 0.0),
	('Johns Hopkins University', 3.5),
	('Johnson C Smith University', 0.0),
	('Johnson University Florida', 14.4),
	('Keiser University-Ft Lauderdale', 4.0),
	('Kentucky Christian University', -3.4),
	('Kenyon College', 3.7),
	('La Sierra University', 2.7),
	('Lafayette College', 3.8),
	('Lane College', 6.5),
	('Lehigh University', 3.1),
	('LeTourneau University', 4.5),
	('Liberty University', 14.9),
	('Lincoln Christian University', 0.0),
	('Luther Rice University & Seminary', 4.3),
	('Macalester College', 4.0),
	('Maharishi University of Management', 0.0),
	('Manhattan School of Music', 3.4),
	('Maria College of Albany', 8.3),
	('Marist College', 4.2),
	('Marygrove College', 2.4),
	('Massachusetts Institute of Technology', 3.5),
	('Memphis College of Art', 5.0),
	('Menlo College', 1.1),
	('Methodist College', 0.0),
	('Mid-Atlantic Christian University', 5.3),
	('Middlebury College', 1.6),
	('Missouri Valley College', -2.1),
	('Montreat College', 0.0),
	('Mount Mary University', 3.0),
	('New York School of Interior Design', 24.2),
	('New York University', 2.9),
	('Northeastern University', 4.2),
	('Northwestern University', 3.8),
	('Northwood University-Florida', 4.5),
	('Notre Dame of Maryland University', 0.0),
	('Nova Southeastern University', 5.1),
	('Oakwood University', 3.0),
	('Oberlin College', 3.9),
	('Occidental College', 1.9),
	('Ohio Dominican University', 1.7),
	('Ohio Valley University', 2.7),
	('Our Lady of the Lake University', 2.7),
	('Pacific Union College', 2.4),
	('Paine College', 0.0),
	('Pennsylvania College of Art and Design', 6.4),
	('Pennsylvania College of Health Sciences', 7.2),
	('Pepperdine University', 4.0),
	('Pfeiffer University', 7.1),
	('Piedmont International University', -25.3),
	('Pitzer College', 4.4),
	('Pomona College', 5.2),
	('Pontifical Catholic University of Puerto Rico-Arecibo', 3.4),
	('Princeton University', 4.1),
	('Providence Christian College', 6.0),
	('Reed College', 3.8),
	('Rensselaer Polytechnic Institute', 3.5),
	('Rhode Island School of Design', 3.9),
	('Rice University', 4.2),
	('Robert Morris University Illinois', 3.9),
	('Rochester College', 2.8),
	('Rust College', 4.3),
	('Saint Xavier University', 3.9),
	('San Francisco Conservatory of Music', 3.6),
	('Santa Clara University', 3.9),
	('Scripps College', 4.0),
	('Shimer College', 3.1),
	('Shorter University-College of Adult & Professional Programs', 0.0),
	('Silver Lake College of the Holy Family', 5.0),
	('Skidmore College', 3.5),
	('Smith College', 3.7),
	('Soka University of America', 3.7),
	('Southeastern University', 11.1),
	('Southern Virginia University', -22.8),
	('Southwestern Adventist University', 4.4),
	('Southwestern Assemblies of God University', 4.2),
	('Southwestern University', 2.5),
	('Spalding University', 2.3),
	('St Lawrence University', 3.6),
	("St Vincent's College", -17.6),
	('Stanford University', 4.5),
	('Sterling College', 3.5),
	('Stevens Institute of Technology', 2.0),
	('Summit Christian College', 15.8),
	('Swarthmore College', 3.0),
	('Texas Christian University', 5.5),
	('Texas Wesleyan University', 5.0),
	('The Boston Conservatory', 3.5),
	('The College of New Rochelle', 3.3),
	('The Juilliard School', 3.4),
	('The New England Conservatory of Music', 3.6),
	('Toccoa Falls College', 3.7),
	('Tougaloo College', -0.1),
	('Touro College', 0.3),
	('Touro University Worldwide', -13.5),
	('Trinity Bible College', 5.2),
	('Trinity College', 3.3),
	('Trinity University', 4.4),
	('Tufts University', 4.4),
	('Tulane University of Louisiana', 2.9),
	('Tuskegee University', 3.5),
	('Union College', 3.4),
	('Universidad Central Del Caribe', 0.0),
	('Universidad del Sagrado Corazon', 2.2),
	('University of Chicago', 3.9),
	('University of La Verne', 5.0),
	('University of Miami', 3.5),
	('University of Mount Olive', 2.9),
	('University of Notre Dame', 3.7),
	('University of Pennsylvania', 3.9),
	('University of Richmond', 3.0),
	('University of Rochester', 3.5),
	('University of Saint Mary', 5.5),
	('University of San Diego', 3.7),
	('University of Southern California', 4.3),
	('University of Tulsa', 2.9),
	('Vanderbilt University', 2.0),
	('Vassar College', 3.5),
	('Villanova University', 3.5),
	('Virginia Union University', 0.0),
	('Visible Music College', -10.9),
	('Wake Forest University', 3.3),
	('Warner University', 2.9),
	('Washington & Jefferson College', 4.0),
	('Washington Adventist University', 1.8),
	('Washington and Lee University', 2.5),
	('Washington University in St Louis', 3.6),
	('Watkins College of Art Design & Film', 2.7),
	('Webb Institute', 2.9),
	('Wellesley College', 3.5),
	('Wesleyan University', 2.2),
	('Whitman College', 3.0),
	('Wilberforce University', 0.0),
	('Williams College', 3.7),
	('Wilson College', -17.0),
	('Worcester Polytechnic Institute', 3.4),
	('Yale University', 4.1),
	("Yeshiva D'monsey Rabbinical College", 8.3),
	('York College', 3.1),
	('York College Pennsylvania', 3.6)

	)

with con: 
	cur = con.cursor()
	cur.execute("DROP TABLE IF EXISTS Private")
	cur.execute("CREATE TABLE Private(id TEXT, tuition_percentage_change INT)")

	cur.executemany("INSERT INTO Private VALUES(?, ?)", menu)

