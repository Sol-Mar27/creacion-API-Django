from .serializers import TipoAlojamientoSerializer, AlojamientoSerializer, TipoHabitacionSerializer
from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from apps.alojamientos.models import TipoAlojamiento, TipoHabitacion, Alojamiento

class TipoAlojamientoViewset(viewsets.ModelViewSet):
    queryset = TipoAlojamiento.objects.activos() #que son consultas se van a poder hacer(conjunto de datos)
    serializer_class = TipoAlojamientoSerializer #como los va a convertir
    
    def create(self, request, *args, **kwargs):                
        serializer = self.get_serializer(data=request.data) 
        serializer.is_valid(raise_exception=True)  
        self.perform_create(serializer)  

        return Response({
            "message": "Tipo de Alojamiento creado.",
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
            'message': 'Tipo de alojamiento ha sido Eliminado.'
        }, status=status.HTTP_204_NO_CONTENT)
    

class TipoHabitacionViewset(viewsets.ModelViewSet):
    queryset = TipoHabitacion.objects.activos() #que son consultas se van a poder hacer(conjunto de datos)
    serializer_class = TipoHabitacionSerializer #como los va a convertir
    
    def create(self, request, *args, **kwargs):                
        serializer = self.get_serializer(data=request.data) 
        serializer.is_valid(raise_exception=True)  
        self.perform_create(serializer)  

        return Response({
            "message": "Tipo de habitacion creado.",
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
            'message': 'Tipo de habitacion ha sido Eliminado.'
        }, status=status.HTTP_204_NO_CONTENT)
        
class AlojamientoViewset(viewsets.ModelViewSet):
    queryset = Alojamiento.objects.activos() #que son consultas se van a poder hacer(conjunto de datos)
    serializer_class = AlojamientoSerializer #como los va a convertir
    
    def create(self, request, *args, **kwargs):                
        serializer = self.get_serializer(data=request.data) 
        serializer.is_valid(raise_exception=True)  
        self.perform_create(serializer)  

        return Response({
            "message": "Alojamiento creado.",
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
            'message': 'Alojamiento ha sido Eliminado.'
        }, status=status.HTTP_204_NO_CONTENT)