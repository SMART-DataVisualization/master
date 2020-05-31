#include "stdafx.h"
#include "Blank.h"

void Blank::display() 
{
	glClearColor(194 / 255.0f, 206 / 255.0f, 218 / 255.0f, 0.0f);		//194, 206, 218. VisCanvas background color.
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
	glLoadIdentity();
}