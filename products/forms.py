from django import forms
from products.models import Category, SubCategory, Product


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'slug', 'description', 'status']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Category Name'}),
            'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Slug'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description', 'rows': 3}),
            'status': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def clean_slug(self):
        slug = self.cleaned_data['slug']
        if Category.objects.filter(slug=slug).exists():
            raise forms.ValidationError("Slug already exists")
        return slug


class SubCategoryForm(forms.ModelForm):
    class Meta:
        model = SubCategory
        fields = ['category', 'name', 'slug', 'status']
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sub-Category Name'}),
            'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Slug'}),
            'status': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    
    def clean_slug(self):
        slug = self.cleaned_data['slug']
        if SubCategory.objects.filter(slug=slug).exists():
            raise forms.ValidationError("Slug already exists")
        return slug


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['subcategory', 'name', 'sku', 'price', 'stock', 'description', 'image']
        widgets = {
            'subcategory': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Product Name'}),
            'sku': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'SKU'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Price'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Stock Quantity'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description', 'rows': 3}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }

   
    def clean_sku(self):
        sku = self.cleaned_data['sku']
        if Product.objects.filter(sku=sku).exists():
            raise forms.ValidationError("SKU already exists")
        return sku
