///-------------------------------------------------------------------------------------------------
// file:	TimeSeries_Dist.h
//
// summary:	Declares the time series distance class
///-------------------------------------------------------------------------------------------------

#include "stdafx.h"
#include "ClassData.h"
#include "FileHandling.h"

#pragma once

////////////////////////////////////////////////////////////////////////////////////////////////////
/// <summary>	A time series distance. </summary>
///
/// <author> Phillipe Shin & Allyn Vo 02/25/2019 </author>
/// <editor> Paul Collet </editor>
////////////////////////////////////////////////////////////////////////////////////////////////////

class TimeSeries_Dist
{

public:
	/// <summary>	The converted values. </summary>
	/// <summary>	The converted values. </summary>
	std::vector<std::vector<float> > convertedValues;

	/// <summary>	The data. </summary>
	ClassData data;
	/// <summary>	The new file. </summary>
	FileHandling newFile;

	////////////////////////////////////////////////////////////////////////////////////////////////////
	/// <summary>	Default constructor. </summary>
	///
	/// <author> Phillipe Shin & Allyn Vo 02/25/2019 </author>
	/// <editor> Paul Collet </editor>
	////////////////////////////////////////////////////////////////////////////////////////////////////

	TimeSeries_Dist() {};

	////////////////////////////////////////////////////////////////////////////////////////////////////
	/// <summary>	Constructor. </summary>
	///
	/// <author> Phillipe Shin & Allyn Vo 02/25/2019 </author>
	/// <editor> Paul Collet </editor>
	///
	/// <param name="parameter1">	[in,out] The first parameter. </param>
	/// <param name="parameter2">	The second parameter. </param>
	/// <param name="parameter3">	The third parameter. </param>
	////////////////////////////////////////////////////////////////////////////////////////////////////

	TimeSeries_Dist(ClassData&, double, double);

	////////////////////////////////////////////////////////////////////////////////////////////////////
	/// <summary>	Sort graph 2. </summary>
	///
	/// <author> Phillipe Shin & Allyn Vo 02/25/2019 </author>
	/// <editor> Paul Collet </editor>
	////////////////////////////////////////////////////////////////////////////////////////////////////

	void sortGraph2();

	////////////////////////////////////////////////////////////////////////////////////////////////////
	/// <summary>	Sort distances. </summary>
	///
	/// <author> Phillipe Shin & Allyn Vo 02/25/2019 </author>
	/// <editor> Paul Collet </editor>
	////////////////////////////////////////////////////////////////////////////////////////////////////

	void sortDistances();

	////////////////////////////////////////////////////////////////////////////////////////////////////
	/// <summary>	Normalize data. </summary>
	///
	/// <author> Phillipe Shin & Allyn Vo 02/25/2019 </author>
	/// <editor> Paul Collet </editor>
	////////////////////////////////////////////////////////////////////////////////////////////////////

	void normalizeData();

	////////////////////////////////////////////////////////////////////////////////////////////////////
	/// <summary>	Fill graph locations. </summary>
	///
	/// <author> Phillipe Shin & Allyn Vo 02/25/2019 </author>
	/// <editor> Paul Collet </editor>
	////////////////////////////////////////////////////////////////////////////////////////////////////

	void fillGraphLocations();

	////////////////////////////////////////////////////////////////////////////////////////////////////
	/// <summary>	Draw data. </summary>
	///
	/// <author> Phillipe Shin & Allyn Vo 02/25/2019 </author>
	/// <editor> Paul Collet </editor>
	///
	/// <param name="x1">   	The first x value. </param>
	/// <param name="y1">   	The first y value. </param>
	/// <param name="index">	Zero-based index of the. </param>
	////////////////////////////////////////////////////////////////////////////////////////////////////

	void drawData(float x1, float y1, int index);
	void display();

};