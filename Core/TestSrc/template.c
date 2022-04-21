#include "unity.h"
//#include "unity_internals.h"

void setUp (void) {} /* Is run before every test, put unit init calls here. */
void tearDown (void) {} /* Is run after every test, put unit clean-up calls here. */
void test1(void)
{
	//TEST_ASSERT_EQUAL_HEX8(0, 0);
}

int main(void)
{
 	 UNITY_BEGIN();

 	 RUN_TEST(test1);

 	return UNITY_END();
}
