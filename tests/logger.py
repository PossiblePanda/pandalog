from pandalog import logger

def test_haversine():
	assert logger.haversine(36.12, -86.67, 33.94, -118.40) == 2887.2599506071106