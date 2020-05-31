#include "stdafx.h"
#include "NetworkGraph.h"


NetworkGraph::NetworkGraph(ClassData &given, double worldW, double worldH)
{
	this->data = given;

	data.worldWidth = worldW;
	data.worldHeight = worldH;

	data.xmax = 0;
	data.ymax = 0;

	newFile.openFile(data);
	newFile.sortGraph(data);

	data.classsize = int(data.xdata[0].size());

	data.graphwidth = worldW / 2.0;										// Width size for each graph
	data.graphheight = worldH / 2.0;									// Height size for each graph

	//////////////////////////////////////////////////////////////////////////////////////////////

	display();
}

void NetworkGraph::drawData(float radius)
{
	float degInRad;
	float classRadius = radius / data.classsize;
	float theta = 360 / data.classsize;
	std::vector<float> xx, yy;

	// outer circle
	for (float i = 0; i < 360; i += theta)
	{
		degInRad = i * DEG2RAD;

		xx.push_back(cos(degInRad) * radius);
		yy.push_back(sin(degInRad) * radius);
	}

	// connecting parallel lines
	int k = 1;
	for (int j = 0; j < (signed)data.classsize - 1; j++)
	{
		for (int i = k; i < (signed)xx.size(); i++)
		{
			glLineWidth(10);
			glBegin(GL_LINES);
				glVertex2f(xx[j], yy[j]);
				glVertex2f(xx[i], yy[i]);
			glEnd();

			glColor4f(1, 1, 1, 1);
			glLineWidth(6);
			glBegin(GL_LINES);
				glVertex2f(xx[j], yy[j]);
				glVertex2f(xx[i], yy[i]);
			glEnd();
			glColor4f(0, 0, 0, 1);
		}

		k++;
	}

	// classes circles
	for (int i = 0; i < (signed)data.classsize; i++)
	{
		glTranslatef(xx[i], yy[i], 0.0f);

		glLineWidth(5);
			drawCircle(classRadius, 0);

		glLineWidth(.25);
			drawCircle(classRadius, 2);

		glTranslatef(-xx[i], -yy[i], 0.0f);
	}

	// direction indicators
	glLineWidth(1);
	float x, y;
	double offset = data.classsize * 0.015;
	double newRad = classRadius + (classRadius * (offset + 0.02));

	for (int j = 0; j < (signed)data.classsize; j++)
	{
		for (int i = 0; i < (signed)data.classsize; i++)
		{
			if (i != j)
			{
				theta = atan2(yy[j] - yy[i], xx[j] - xx[i]);
				x = xx[i] + newRad * cos(theta + offset);
				y = yy[i] + newRad * sin(theta + offset);

				glTranslatef(x, y, 0.0f);
				drawCircle((classRadius * offset), 1);
				glTranslatef(-x, -y, 0.0f);
			}
		}
	}
	//glFlush();
	glPopMatrix();
}
	

void NetworkGraph::drawCircle(float radius, int filled)
{
	float degInRad;

	if (filled == 0)
	{
		glBegin(GL_LINE_STRIP);		
	}
	else
	{
		if (filled > 1)
		{
			glColor4f(1, 1, 1, 1);
		}

		glBegin(GL_POLYGON);
	}

	for (int i = 0; i < 360; i++)
	{
		degInRad = i * DEG2RAD;
		glVertex2f(cos(degInRad) * radius, sin(degInRad) * radius);
	}

	if (filled > 1)
		glColor4f(0, 0, 0, 1);

	glEnd();
}


void NetworkGraph::display()
{
	glClearColor(194 / 255.0f, 206 / 255.0f, 218 / 255.0f, 0.0f);		//194, 206, 218. VisCanvas background color.
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();

	/* Adjust the windows aspect ratio? */
	glOrtho(data.leftWidth, data.worldWidth, data.worldHeight, data.bottomHeight, -1, 1);

	glMatrixMode(GL_MODELVIEW);
	glLoadIdentity(); // Reset the model-view matrix

	glEnable(GL_BLEND);
	glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);
	glEnable(GL_LINE_SMOOTH);

	glTranslatef((data.graphwidth / 2), (data.graphheight / 2), 0.0f);
	glScalef(data.graphwidth, data.graphheight, 0.0f);

	drawData(.75);

}


void NetworkGraph::zoom(double factor)
{
	data.graphwidth *= factor;
	data.graphheight *= factor;
}


void NetworkGraph::zoom_at(double x, double y, double factor) // Zooms in by a factor and towards the mouse location
{
	data.pan_x += (data.worldWidth / 2 - x) / 2;
	data.pan_y += (data.worldHeight / 2 - y) / 2;
	zoom(factor);
}



