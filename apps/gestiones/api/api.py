from .serializers import ValoracionComentarioSerializer, RedSocialSerializer
from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from apps.gestiones.models import RedSocial, ValoracionComentario

class RedSocialViewset(viewsets.ModelViewSet):
    queryset = RedSocial.objects.activos() #que son consultas se van a poder hacer(conjunto de datos)
    serializer_class = RedSocialSerializer #como los va a convertir
    
    def create(self, request, *args, **kwargs):                
        serializer = self.get_serializer(data=request.data) 
        serializer.is_valid(raise_exception=True)  
        self.perform_create(serializer)  

        return Response({
            "message": "Red Social creado.",
            "created_data": serializer.data
        }, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs): 
        partial = kwargs.pop('partial', False)
        instance = self.get_object()   
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({
            "message": "Los datos han sido actualizados",
            "updated_data": serializer.data 
        }, status=status.HTTP_200_OK)
    
    def destroy(self, request, *args, **kwargs):
        usuario = self.get_object()
        usuario.estado = False
        usuario.is_active = False  
        usuario.save()

        return Response({
            'status': 'success',
            'message': 'Red Social ha sido Eliminado.'
        }, status=status.HTTP_204_NO_CONTENT)
    

class ValoracionComentarioViewset(viewsets.ModelViewSet):
    queryset = ValoracionComentario.objects.activos() #que son consultas se van a poder hacer(conjunto de datos)
    serializer_class = ValoracionComentarioSerializer #como los va a convertir
    
    def create(self, request, *args, **kwargs):                
        serializer = self.get_serializer(data=request.data) 
        serializer.is_valid(raise_exception=True)  
        self.perform_create(serializer)  

        return Response({
            "message": "Valoracion Comentario creado.",
            "created_data": serializer.data
        }, status=status.HTTP_201_CREATED)  

    def update(self, request, *args, **kwargs): 
        partial = kwargs.pop('partial', False)
        instance = self.get_object()   
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({
            "message": "Los datos han sido actualizados",
            "updated_data": serializer.data 
        }, status=status.HTTP_200_OK)
    
    def destroy(self, request, *args, **kwargs):
        usuario = self.get_object()
        usuario.estado = False
        usuario.is_active = False  
        usuario.save()

        return Response({
            'status': 'success',
            'message': 'El Valoracion Comentario ha sido Eliminado.'
        }, status=status.HTTP_204_NO_CONTENT)