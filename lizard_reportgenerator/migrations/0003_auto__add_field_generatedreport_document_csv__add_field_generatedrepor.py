# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'GeneratedReport.document_csv'
        db.add_column('lizard_reportgenerator_generatedreport', 'document_csv', self.gf('django.db.models.fields.CharField')(default='', max_length=255), keep_default=False)

        # Adding field 'GeneratedReport.document_xls'
        db.add_column('lizard_reportgenerator_generatedreport', 'document_xls', self.gf('django.db.models.fields.CharField')(default='', max_length=255), keep_default=False)

        # Adding field 'ReportTemplate.generation_module'
        db.add_column('lizard_reportgenerator_reporttemplate', 'generation_module', self.gf('django.db.models.fields.CharField')(default='lizard_', max_length=255), keep_default=False)

        # Adding field 'ReportTemplate.generation_function'
        db.add_column('lizard_reportgenerator_reporttemplate', 'generation_function', self.gf('django.db.models.fields.CharField')(default='todo', max_length=255), keep_default=False)

        # Adding field 'ReportTemplate.extra_arguments'
        db.add_column('lizard_reportgenerator_reporttemplate', 'extra_arguments', self.gf('django.db.models.fields.CharField')(default='{}', max_length=255), keep_default=False)

        # Adding field 'ReportTemplate.rtf_supported'
        db.add_column('lizard_reportgenerator_reporttemplate', 'rtf_supported', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # Adding field 'ReportTemplate.pdf_supported'
        db.add_column('lizard_reportgenerator_reporttemplate', 'pdf_supported', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # Adding field 'ReportTemplate.csv_supported'
        db.add_column('lizard_reportgenerator_reporttemplate', 'csv_supported', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # Adding field 'ReportTemplate.xls_supported'
        db.add_column('lizard_reportgenerator_reporttemplate', 'xls_supported', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'GeneratedReport.document_csv'
        db.delete_column('lizard_reportgenerator_generatedreport', 'document_csv')

        # Deleting field 'GeneratedReport.document_xls'
        db.delete_column('lizard_reportgenerator_generatedreport', 'document_xls')

        # Deleting field 'ReportTemplate.generation_module'
        db.delete_column('lizard_reportgenerator_reporttemplate', 'generation_module')

        # Deleting field 'ReportTemplate.generation_function'
        db.delete_column('lizard_reportgenerator_reporttemplate', 'generation_function')

        # Deleting field 'ReportTemplate.extra_arguments'
        db.delete_column('lizard_reportgenerator_reporttemplate', 'extra_arguments')

        # Deleting field 'ReportTemplate.rtf_supported'
        db.delete_column('lizard_reportgenerator_reporttemplate', 'rtf_supported')

        # Deleting field 'ReportTemplate.pdf_supported'
        db.delete_column('lizard_reportgenerator_reporttemplate', 'pdf_supported')

        # Deleting field 'ReportTemplate.csv_supported'
        db.delete_column('lizard_reportgenerator_reporttemplate', 'csv_supported')

        # Deleting field 'ReportTemplate.xls_supported'
        db.delete_column('lizard_reportgenerator_reporttemplate', 'xls_supported')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'lizard_area.area': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Area', '_ormbases': ['lizard_area.Communique']},
            'area_class': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'communique_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['lizard_area.Communique']", 'unique': 'True', 'primary_key': 'True'}),
            'data_administrator': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lizard_area.DataAdministrator']"}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lizard_area.Area']", 'null': 'True', 'blank': 'True'})
        },
        'lizard_area.communique': {
            'Meta': {'object_name': 'Communique', '_ormbases': ['lizard_geo.GeoObject']},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'geoobject_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['lizard_geo.GeoObject']", 'unique': 'True', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'lizard_area.dataadministrator': {
            'Meta': {'object_name': 'DataAdministrator'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'})
        },
        'lizard_geo.geoobject': {
            'Meta': {'object_name': 'GeoObject'},
            'geo_object_group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lizard_geo.GeoObjectGroup']"}),
            'geometry': ('django.contrib.gis.db.models.fields.GeometryField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ident': ('django.db.models.fields.CharField', [], {'max_length': '80'})
        },
        'lizard_geo.geoobjectgroup': {
            'Meta': {'object_name': 'GeoObjectGroup'},
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'source_log': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'lizard_reportgenerator.generatedreport': {
            'Meta': {'object_name': 'GeneratedReport'},
            'area': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lizard_area.Area']"}),
            'data_set': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lizard_security.DataSet']", 'null': 'True', 'blank': 'True'}),
            'document_csv': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'document_pdf': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'document_rtf': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'document_xls': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'generated_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 1, 27, 20, 17, 44, 947218)', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'template': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lizard_reportgenerator.ReportTemplate']"}),
            'visible': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        'lizard_reportgenerator.reporttemplate': {
            'Meta': {'object_name': 'ReportTemplate'},
            'csv_supported': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'extra_arguments': ('django.db.models.fields.CharField', [], {'default': "'{}'", 'max_length': '255'}),
            'generation_function': ('django.db.models.fields.CharField', [], {'default': "'todo'", 'max_length': '255'}),
            'generation_module': ('django.db.models.fields.CharField', [], {'default': "'lizard_'", 'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kind': ('django.db.models.fields.CharField', [], {'default': "'algemeen'", 'max_length': '255'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'pdf_supported': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'rtf_supported': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'xls_supported': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'lizard_security.dataset': {
            'Meta': {'ordering': "['name']", 'object_name': 'DataSet'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'})
        }
    }

    complete_apps = ['lizard_reportgenerator']
