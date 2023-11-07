from odoo import fields, models, api
import uuid

class SurveyWarehouse(models.Model):
    _inherit = 'survey.user_input'
    
    picking_id = fields.Many2one('stock.picking', readonly=True)
    fake_create_datetime = fields.Datetime()


    
class WarehousePicking(models.Model):
    _inherit = 'stock.picking'

    has_matching_survey = fields.Integer(compute='_compute_has_matching_survey')

    def create_survey_pick(self):
        if self.backorder_id:
            return
        print("Valore di id:", id)
        token = str(uuid.uuid4())
        survey_data = {
        'fake_create_datetime': self.scheduled_date,
        'activity_ids': [],
        'activity_state': False,
        'activity_user_id': False,
        'activity_type_id': False,
        'activity_type_icon': False,
        'activity_date_deadline': False,
        'my_activity_date_deadline': False,
        'activity_summary': False,
        'activity_exception_decoration': False,
        'activity_exception_icon': False,
        'has_message': True,
        'message_needaction': False,
        'message_needaction_counter': 0,
        'message_has_error': False,
        'message_has_error_counter': 0,
        'message_attachment_count': 0,
        'message_main_attachment_id': False,
        'website_message_ids': [],
        'message_has_sms_error': False,
        'survey_id': 24,
        'scoring_type': 'scoring_with_answers',
        'deadline': False,
        'state': 'new',
        'test_entry': False,
        'is_attempts_limited': False,
        'attempts_limit': 1,
        'attempts_count': 1,
        'attempts_number': 1,
        'survey_time_limit_reached': False,
        'access_token': token,
        'invite_token': False,
        'partner_id': self.env.user.partner_id.id, # Da pescare uil partner id che esegue l'azione
        'scoring_success': True,
        'is_session_answer': False,
        'question_time_limit_reached': False,
        'ticket_ids': [],
        'trip_id': False,
        'trip_type_survey_generator_id': False,
        'force_success': False,
        'trip_vehicle_manager_id': False,
        'vehicle_id': False,
        'picking_id': self.id,
        }
        
        # Crea le risposte alle domande nel questionario
        user_input = self.env['survey.user_input'].create(survey_data)
        
    
    def create_survey_pick_and_answers(self):
        if self.backorder_id:
            return
        if self.picking_type_id.id not in [49, 50]:
            return
        print("Valore di id:", id)
        token = str(uuid.uuid4())
        survey_data = {
        'fake_create_datetime': self.scheduled_date,
        'activity_ids': [],
        'activity_state': False,
        'activity_user_id': False,
        'activity_type_id': False,
        'activity_type_icon': False,
        'activity_date_deadline': False,
        'my_activity_date_deadline': False,
        'activity_summary': False,
        'activity_exception_decoration': False,
        'activity_exception_icon': False,
        'has_message': True,
        'message_needaction': False,
        'message_needaction_counter': 0,
        'message_has_error': False,
        'message_has_error_counter': 0,
        'message_attachment_count': 0,
        'message_main_attachment_id': False,
        'website_message_ids': [],
        'message_has_sms_error': False,
        'survey_id': 24,
        'scoring_type': 'scoring_with_answers',
        'deadline': False,
        'state': 'done',
        'test_entry': False,
        'is_attempts_limited': False,
        'attempts_limit': 1,
        'attempts_count': 1,
        'attempts_number': 1,
        'survey_time_limit_reached': False,
        'access_token': token,
        'invite_token': False,
        'partner_id': self.env.user.partner_id.id, # Da pescare uil partner id che esegue l'azione
        'scoring_percentage': 70.0,
        'scoring_total': 70.0,
        'scoring_success': True,
        'is_session_answer': False,
        'question_time_limit_reached': False,
        'ticket_ids': [],
        'trip_id': False,
        'trip_type_survey_generator_id': False,
        'force_success': False,
        'trip_vehicle_manager_id': False,
        'vehicle_id': False,
        'picking_id': self.id,
        }
        
        # Crea le risposte alle domande nel questionario
        user_input = self.env['survey.user_input'].create(survey_data)
        
        answer_1 = answer_2 = answer_3 = answer_4 = answer_5 = answer_6 = answer_7 = {
                'user_input_id': user_input.id,
                'page_id': False,
                'question_sequence': 10,
                'skipped': False,
                'answer_type': 'suggestion',
                'value_char_box': False,
                'value_numerical_box': 0.0,
                'value_date': False,
                'value_datetime': False,
                'value_text_box': False,
                'matrix_row_id': False,
                'answer_is_correct': True,
                'display_name': 'Si',
                'value_ans_sh_color': False,
                'value_ans_sh_email': False,
                'value_ans_sh_url': False,
                'value_ans_sh_time': False,
                'value_ans_sh_range': 0,
                'value_ans_sh_week': False,
                'value_ans_sh_month': False,
                'value_ans_sh_password': False,
                'value_ans_sh_file': False,
                'value_ans_sh_file_fname': False,
                'value_ans_sh_signature': False,
                'value_ans_sh_signature_src': False,
                'value_ans_sh_many2one': False,
                'value_ans_sh_many2many': False,
                'value_ans_sh_street': False,
                'value_ans_sh_street2': False,
                'value_ans_sh_zip': False,
                'value_ans_sh_city': False,
                'value_ans_sh_state_id': False,
                'value_ans_sh_country_id': False,
                'value_ans_sh_address': False
            }
        answer_1['question_id'] = 585
        answer_1['suggested_answer_id'] = 793
        answer_1['answer_score'] = 10.0
        user_answer_1 = self.env['survey.user_input.line'].create(answer_1)
        
        answer_2['question_id'] = 586
        answer_2['suggested_answer_id'] = 796
        answer_2['answer_score'] = 10.0
        user_answer_2 = self.env['survey.user_input.line'].create(answer_2)
        
        answer_3['question_id'] = 587
        answer_3['suggested_answer_id'] = 799
        answer_3['answer_score'] = 10.0
        user_answer_3 = self.env['survey.user_input.line'].create(answer_3)
        
        answer_4['question_id'] = 588
        answer_4['suggested_answer_id'] = 802
        answer_4['answer_score'] = 10.0
        user_answer_4 = self.env['survey.user_input.line'].create(answer_4)
        
        answer_5['question_id'] = 589
        answer_5['suggested_answer_id'] = 805
        answer_5['answer_score'] = 10.0
        user_answer_5 = self.env['survey.user_input.line'].create(answer_5)
        
        answer_6['question_id'] = 590
        answer_6['suggested_answer_id'] = 808
        answer_6['answer_score'] = 10.0
        user_answer_6 = self.env['survey.user_input.line'].create(answer_6)
        
        answer_7['question_id'] = 591
        answer_7['suggested_answer_id'] = 811
        answer_7['answer_score'] = 10.0
        user_answer_7 = self.env['survey.user_input.line'].create(answer_7)
        
        return user_input.id      

    
    def search_survey_user_input(self):
        self.ensure_one()
        return {
            'name': ('Sondaggi'),
            'type': 'ir.actions.act_window',
            'res_model': 'survey.user_input',
            'view_mode': 'tree,form',
            'domain': [('picking_id', '=', self.name)],
        }

    def _compute_has_matching_survey(self):
        for survey in self:
            matching_survey = self.env['survey.user_input'].search_count([('picking_id', '=', self.name)])
            survey.has_matching_survey = matching_survey


    def create_survey_picks_and_answers(self):
        for record in self:
            record.create_survey_pick_and_answers()
        return True
    
        
