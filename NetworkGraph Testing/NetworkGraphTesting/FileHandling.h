
#include "stdx.h"
#include "ClassData.h"

#pragma once

class FileHandling
{
public:

	FileHandling();

	void openFile(ClassData&);

	void sortGraph(ClassData&);

	void normalizeData(ClassData &data);

	void normalizeDataV2(ClassData &data);

};

