from django import forms

from .models import Task, Client, Customer, WorkType

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task

        fields = (
            'title',
            'type',
            'description',
            'cost',
            'address',
            'client',
            'customer',
            'executor',
            'status'
            # 'is_done',
            # 'is_canceled',
            # 'is_invoiced',
            # 'is_paid',
        )

        widgets = {
            'title': forms.TextInput(attrs={
                'type': 'text',
                'class':'form-control',
                'id': 'formGroupExampleInput',
                # 'placeholder': 'Введите наименование работ'
            }), 
            'type': forms.Select(attrs={
                'class':'form-select',
                'aria-label': 'Выберите тип работ'
            }),
            'description': forms.Textarea(attrs={
                'type': 'text',
                'class':'form-control',
                'id': 'floatingTextarea',
                # 'placeholder': 'Введите описание работ'
            }), 
            'cost': forms.TextInput(attrs={
                'type': 'text',
                'class':'form-control',
                'id': 'formGroupExampleInput',
                # 'placeholder': 'Введите стоимость работ'
            }), 

            'address': forms.Textarea(attrs={
                'type': 'text',
                'class':'form-control',
                'id': 'floatingTextarea',
                # 'placeholder': 'Введите адрес объекта'
            }), 
            'client': forms.Select(attrs={
                'class':'form-select',
                'id': 'inputGroupSelect02'
            }),
            'customer': forms.Select(attrs={
                'class':'form-select',
                'aria-label': 'Выберите тип работ'
            }),
            'executor': forms.Select(attrs={
                'class':'form-select',
                'aria-label': 'Выберите тип работ'
            }),
            'status': forms.Select(attrs={
                'class':'form-select',
                'aria-label': 'Установите статус задачи'
            }),


            # 'is_done': forms.CheckboxInput(attrs={
            #     'class':'form-check-input',
            #     'type': 'radio',
            #     'id': 'flexRadioDefault1',
            #     'name': 'flexRadioDefault'
            # }),
            # 'is_canceled': forms.CheckboxInput(attrs={
            #     'class':'form-check-input',
            #     'type': 'radio',
            #     'id': 'flexRadioDefault2',
            #     'name': 'flexRadioDefault'
            # }),
            # 'is_invoiced': forms.CheckboxInput(attrs={
            #     'class':'form-check-input',
            #     'type': 'radio',
            #     'id': 'flexRadioDefault3',
            #     'name': 'flexRadioDefault'
            # }),
            # 'is_paid': forms.CheckboxInput(attrs={
            #     'class':'form-check-input',
            #     'type': 'radio',
            #     'id': 'flexRadioDefault4',
            #     'name': 'flexRadioDefault'
            # }),


        }
        
    
class ClientForm(forms.ModelForm):
    class Meta:
        model = Client

        fields = (
            'name',
            'contact_person_name',
            'contact_person_phone',
            'contact_person_email',
            'address',
        )

        widgets = {
            'name': forms.TextInput(attrs={
                'type': 'text',
                'class':'form-control',
                'id': 'formGroupExampleInput',
                # 'placeholder': 'Введите название клиента'
            }), 
            'contact_person_name': forms.TextInput(attrs={
                'type': 'text',
                'class':'form-control',
                'id': 'formGroupExampleInput',
                # 'placeholder': 'Введите имя контактного лица'
            }), 
            'contact_person_phone': forms.TextInput(attrs={
                'type': 'text',
                'class':'form-control',
                'id': 'formGroupExampleInput',
                # 'placeholder': 'Введите контактный телефон'
            }), 
            'contact_person_email': forms.TextInput(attrs={
                'type': 'text',
                'class':'form-control',
                'id': 'formGroupExampleInput',
                # 'placeholder': 'Введите контактный емейл'
            }), 
            'address': forms.Textarea(attrs={
                'type': 'text',
                'class':'form-control',
                'id': 'floatingTextarea',
                # 'placeholder': 'Введите адрес клиента'
            }), 
        }


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer

        fields = (
            'name',
            'contact_person_name',
            'contact_person_phone',
            'contact_person_email',
            'is_operator',
            'address',
        )

        widgets = {
            'name': forms.TextInput(attrs={
                'type': 'text',
                'class':'form-control',
                'id': 'formGroupExampleInput',
                # 'placeholder': 'Введите название клиента'
            }), 
            'is_operator': forms.CheckboxInput(attrs={
                'class':'form-check-input',
                'type': 'checkbox',
                'id': 'flexCheckDefault',
            }), 
            'contact_person_name': forms.TextInput(attrs={
                'type': 'text',
                'class':'form-control',
                'id': 'formGroupExampleInput',
                # 'placeholder': 'Введите имя контактного лица'
            }), 
            'contact_person_phone': forms.TextInput(attrs={
                'type': 'text',
                'class':'form-control',
                'id': 'formGroupExampleInput',
                # 'placeholder': 'Введите контактный телефон'
            }), 
            'contact_person_email': forms.TextInput(attrs={
                'type': 'text',
                'class':'form-control',
                'id': 'formGroupExampleInput',
                # 'placeholder': 'Введите контактный емейл'
            }), 
            'address': forms.Textarea(attrs={
                'type': 'text',
                'class':'form-control',
                'id': 'floatingTextarea',
                # 'placeholder': 'Введите адрес клиента'
            }), 
        }


class WorkTypeForm(forms.ModelForm):
    class Meta:
        model = WorkType

        fields = (
            'title',
            'description',
            'base_price',
        )

        widgets = {
            'title': forms.TextInput(attrs={
                'type': 'text',
                'class':'form-control',
                'id': 'formGroupExampleInput',
            }), 
            'description': forms.Textarea(attrs={
                'type': 'text',
                'class':'form-control',
                'id': 'floatingTextarea',
            }), 
            'base_price': forms.TextInput(attrs={
                'type': 'text',
                'class':'form-control',
                'id': 'formGroupExampleInput',
            }), 

        }

    