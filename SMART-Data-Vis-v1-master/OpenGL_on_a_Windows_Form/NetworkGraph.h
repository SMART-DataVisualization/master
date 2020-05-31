
#include "stdafx.h"
#include "ClassData.h"
#include "FileHandling.h"

#pragma once
class NetworkGraph
{
	const float DEG2RAD = 3.14159 / 180;

public:

	ClassData data;

	FileHandling newFile;

	NetworkGraph() {};

	NetworkGraph(ClassData&, double, double);

	void drawCircle(float radius, int filled);

	void drawData(float radius);

	void display();

	void zoom(double factor);
	void zoom_at(double x, double y, double factor);
};


