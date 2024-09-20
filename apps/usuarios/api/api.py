from apps.usuarios.models import Idioma, Nacionalidad, TipoDeCuenta, TipoDocumento, Usuario
from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from .serializers import IdiomaSerializer, NacionalidadSerializer, TipoDeCuentaSerializer, TipoDocumentoSerializer, UsuarioSerializer 

class IdiomaViewset(viewsets.ModelViewSet):
    queryset = Idioma.objects.activos() #que son consultas se van a poder hacer(conjunto de datos)
    serializer_class = IdiomaSerializer #como los va a convertir
    
    def create(self, request, *args, **kwargs):                
        serializer = self.get_serializer(data=request.data) 
        serializer.is_valid(raise_exception=True)  
        self.perform_create(serializer)  

        return Response({
            "message": "Idioma creado.",
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
            'message': 'El Idioma ha sido Eliminado.'
        }, status=status.HTTP_204_NO_CONTENT)
    
    
class NacionalidadViewSet(viewsets.ModelViewSet):
    queryset = Nacionalidad.objects.activos()
    serializer_class = NacionalidadSerializer
    
    def create(self, request, *args, **kwargs):                
        serializer = self.get_serializer(data=request.data) 
        serializer.is_valid(raise_exception=True)  
        self.perform_create(serializer)  

        return Response({
            "message": "Nacionalidad creada.",
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
            'message': 'La Nacionalidad ha sido Eliminada.'
        }, status=status.HTTP_204_NO_CONTENT)

class TipoDeCuentaViewSet(viewsets.ModelViewSet):
    queryset = TipoDeCuenta.objects.filter(estado=True)
    serializer_class = TipoDeCuentaSerializer
    
    def create(self, request, *args, **kwargs):                
        serializer = self.get_serializer(data=request.data) 
        serializer.is_valid(raise_exception=True)  
        self.perform_create(serializer)  

        return Response({
            "message": "Tipo de Cuenta creada.",
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
            'message': 'Tipo de cuenta ha sido Eliminada.'
        }, status=status.HTTP_204_NO_CONTENT)

class TipoDocumentoViewSet(viewsets.ModelViewSet):
    queryset = TipoDocumento.objects.activos()
    serializer_class = TipoDocumentoSerializer
    
    def create(self, request, *args, **kwargs):                
        serializer = self.get_serializer(data=request.data) 
        serializer.is_valid(raise_exception=True)  
        self.perform_create(serializer)  

        return Response({
            "message": "Tipo de documento creado.",
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
            'message': 'El Tipo de documento ha sido Eliminado.'
        }, status=status.HTTP_204_NO_CONTENT)
    
    
class UsuarioViewSet(viewsets.ModelViewSet):    
    queryset = Usuario.objects.filter(estado=True)
    serializer_class = UsuarioSerializer
    
    # Permite cualquier usuario para el registro (POST)
    def get_permissions(self):
        if self.action in ['create']:
            self.permission_classes = [AllowAny]  # Permitir acceso no autenticado para la creación
        else:
            self.permission_classes = [IsAuthenticated]  # Requiere autenticación para otras acciones
        return super(UsuarioViewSet, self).get_permissions()

    def perform_create(self, serializer):
        """Sobrescribe el método para crear usuarios usando create_user"""
        serializer.save()  # Aquí ya llamará al método `create` del serializer
    
    def create(self, request, *args, **kwargs):                
        serializer = self.get_serializer(data=request.data) 
        serializer.is_valid(raise_exception=True)  
        self.perform_create(serializer)  

        return Response({
            "message": "Usuario creado.",
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
            'message': 'El usuario ha sido Eliminado.'
        }, status=status.HTTP_204_NO_CONTENT)
      

    
