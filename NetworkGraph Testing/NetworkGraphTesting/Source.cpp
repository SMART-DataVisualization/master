#include "stdx.h"
#include "ClassData.h"
#include "FileHandling.h"


const float DEG2RAD = 3.14159 / 180;
const int HEIGHT = 900;
const int WIDTH = 900;

void myInit()
{
	
	glClearColor(1.0, 1.0, 1.0, 1.0);
	glColor4f(0.0f, 0.0f, 0.0f, 1.0f);
	
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	gluOrtho2D(0.0, HEIGHT, 0.0, WIDTH);
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
}

void drawText(std::string str)
{
	// May have to set length to 2 after decimal point for numbers
	int len = str.size();

	glRasterPos2f(-.01 * len, -.01);

	for (int i = 0; i < len; i++)
	{
		glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, str.at(i));
	}
	
}

void drawCircle(float radius, int filled)
{
	float degInRad;

	if (filled == 0)
	{	
		glBegin(GL_LINE_STRIP);
	}
	else 
	{
		glBegin(GL_POLYGON);
	}
		
	for (int i = 0; i < 360; i++)
	{
		degInRad = i * DEG2RAD;
		glVertex2f(cos(degInRad) * radius, sin(degInRad) * radius);
	}
		
	glEnd();
}

void portWeight(ClassData &data, float& pM, float midX, float midY, float wos, float c, int a, int b)
{
	if (pM == 0)
		midX -= wos;
	else if (pM == 90)
		midY -= wos;
	else
	{
		if (pM > 0)
			midX += (wos - (0.01 * pM));
		else
			midX -= (wos - (0.01 * -pM));

		midY = -pM * midX + c;
	}

	glTranslatef(midX, midY, 0.0f);
		drawText(data.values[a + 1][b + 1]);
	glTranslatef(-midX, -midY, 0.0f);
}

void starbWeight(ClassData& data, float& pM, float midX, float midY, float wos, float c, int a, int b)
{
	if (pM == 0)
		midX += wos;
	else if (pM == 90)
		midY += wos;
	else
	{
		if (pM > 0)
			midX -= (wos - (0.01 * pM));
		else
			midX += (wos - (0.01 * -pM));

		midY = -pM * midX + c;
	}

	glTranslatef(midX, midY, 0.0f);
		drawText(data.values[a + 1][b + 1]);
	glTranslatef(-midX, -midY, 0.0f);
}

void graph(float originX, float originY, float radius, ClassData data)
{
	glTranslatef(originX, originY, 0.0f);	
	glScalef(HEIGHT/2, WIDTH/2, 0.0f);

	float degInRad;
	float classRadius = radius / data.numOfClasses;
	float theta = 360 / data.numOfClasses;

	std::vector<float> xx, yy;
	float midX, midY, x, y, m, pM, pC, b;
	float wpos; // weight perpendicular offsets
	float radX, radY;
	int k;
	
	//outer circle
	for (float i = 360; i > 0; i -= 360.0 / data.numOfClasses)
	{
		degInRad = i * DEG2RAD;

		xx.push_back(-cos(degInRad) * radius);
		yy.push_back(-sin(degInRad) * radius);
	}

	wpos = 0.035;

	// connecting lines
	k = 1;
	for (int j = 0; j < data.numOfClasses - 1; j++)
	{
		for (int i = k; i < data.numOfClasses; i++)
		{
			
			glColor3f(0, 0, 0);
			glLineWidth(12);
			glBegin(GL_LINES);		
				glVertex2f(xx[j], yy[j]);
				glVertex2f(xx[i], yy[i]);
			glEnd();

			glColor3f(1, 1, 1);
			glLineWidth(6);
			glBegin(GL_LINES);
				glVertex2f(xx[j], yy[j]);
				glVertex2f(xx[i], yy[i]);	
			glEnd();
			
			glColor3f(0, 0, 0);

			midX = (xx[j] + xx[i]) / 2;

			y = yy[j] - yy[i] + 0.000001;
			x = xx[j] - xx[i] + 0.000001;

			m =  y / x;
			pM = x / y; // Perpendicular slope: midY + pM(midX) = pC

			if (abs(m) > 90)
			{
				pM = 0;
				m = 90;
			}
			if (abs(pM) > 90)
			{
				pM = 90;
				m = 0;
			}

			if (m == 90)
				midY = (yy[j] + yy[i]) / 2 + y / 10;
			else
			{
				b = yy[j] - m * xx[j]; // y-intercept
				midX += x / 10;
				midY = m * midX + b; 
			}
				
			
			pC = midY + pM * midX;
			
			portWeight( data, pM, midX, midY, wpos, pC, j, i);
			starbWeight(data, pM, midX, midY, wpos, pC, i, j);
			
		}

		k++;
	}

	//classes circles
	for (int i = 0; i < data.numOfClasses; i++)
	{	
		glTranslatef(xx[i], yy[i], 0.0f);
	
		glColor3b(0, 0, 0);
		glLineWidth(4);
		drawCircle(classRadius, 0);

		glColor3ub(data.classColor[i][0], data.classColor[i][1], data.classColor[i][2]);

		glLineWidth(1);
		drawCircle(classRadius, 1);

		glColor3ub(1, 1, 1);
		drawText(data.labelTokens[i]);


		glTranslatef(-xx[i], -yy[i], 0.0f);
	}
	 
	// arrows
	glLineWidth(1);
	glColor3b(0, 0, 0);
	
	float offset = data.numOfClasses * 0.015;
	float newRad = classRadius + (classRadius * (offset + 0.02));
	
	for (int j = 0; j < data.numOfClasses; j++)
	{		
		for (int i = 0; i < data.numOfClasses; i++)
		{
			if (i != j)
			{
				theta = atan2(yy[j] - yy[i], xx[j] - xx[i]);
				radX = xx[i] + newRad * cos(theta + offset);
				radY = yy[i] + newRad * sin(theta + offset);	

				glTranslatef(radX, radY, 0.0f);
					drawCircle((classRadius * offset), 1);/////
				glTranslatef(-radX, -radY, 0.0f);
			}
		}
	}
	
	glFlush();
}


void render()
{
	ClassData data;
	FileHandling file;

	data.fileName = "ReportExampleData.csv";
	file.openFile(data);
	file.sortGraph(data);

	data.setClassColors();

	graph(HEIGHT/2, WIDTH/2, .75, data);
}

int main(int argc, char** argv)
{
	glutInit(&argc, argv);
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);
	glutInitWindowSize(HEIGHT, WIDTH);
	glutInitWindowPosition(100, 150);
	glutCreateWindow("Polyline and Polygon");

	glEnable(GL_LINE_SMOOTH);
	glEnable(GL_BLEND);

	glutDisplayFunc(render);
	myInit();
	glutMainLoop();

	glDisable(GL_LINE_SMOOTH);
	glDisable(GL_BLEND);

	return 0;
}