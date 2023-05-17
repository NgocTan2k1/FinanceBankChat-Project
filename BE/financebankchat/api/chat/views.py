
from rest_framework import generics, permissions
from rest_framework.response import Response
from api.chat.serializers import question_serializer
from financebankchat.helper.application_helper import load_json
from financebankchat.helper.npl_helper import add_noise_to_money

from financebankchat.services.chatgpt import process_question
from financebankchat.services.message import encrypt_question


class chat_views(generics.GenericAPIView):
    """
    POST api/v1/chat/
    """
    resource_name = 'chat_api'
    allowed_methods = ['POST']
    serializer_class = question_serializer
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        try:
            success, data = encrypt_question(request.data.get("raw"), request.user)
            if not success:
                return Response(
                    status=400,
                    data={"result": {"message": data, "types": "text"}}
                )
            
            data_json = load_json(data)
            if not data_json:
                return Response(
                    status=400,
                    data={"result": {"message": "Dữ liệu không hợp lệ", "types": "text"}}
                )

            question = add_noise_to_money(str(data_json.pop('question')))
            # data_json = {
            #     "provider_id": [1,2],
            #     "year": [2012,2020],
            #     "stock_id": [1,2]
            # }
            # question = "thông tin nợ"
            results = process_question(question, **data_json)
        except Exception as e:
            return Response(
                status=400,
                data={"result": {"message": "Không tìm thấy thông tin về câu hỏi", "types": "text"}}
            )
        
        return (
            Response({"result": results})
            if results
            else Response(
                status=400,
                data={"result": {"message": "Không tìm thấy thông tin về câu hỏi", "types": "text"}}
            )
        )
