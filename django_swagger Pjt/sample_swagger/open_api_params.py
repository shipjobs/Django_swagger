#sample_swagger/open_api_params.py
from drf_yasg import openapi


##파라메터를 정의 
get_params = [
	openapi.Parameter(
        "start_date",
        openapi.IN_QUERY,
        description="yyyy-mm-dd",
        type=openapi.FORMAT_DATE,
        default=""
    ),
    openapi.Parameter(
        "end_date",
        openapi.IN_QUERY,
        description="yyyy-mm-dd",
        type=openapi.FORMAT_DATE,
        default=""
    )
]

post_params = openapi.Schema(
    type=openapi.TYPE_OBJECT, 
    properties={
        'x': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
        'y': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
    }
)
