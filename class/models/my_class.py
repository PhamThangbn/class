# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ClassStudent(models.Model):
    _name = 'class.student'
    _description = 'Bảng điểm lớp học'

    name = fields.Char(string='Lớp học')
    student_count = fields.Integer(string='Số lượng học sinh')
    avg_student_count = fields.Integer(string='Số lượng học sinh đạt Trung bình', readonly=True, compute='_compute_student_count')
    good_student_count = fields.Integer(string='Số lượng học sinh đạt Khá', readonly=True, compute='_compute_student_count')
    excellent_student_count = fields.Integer(string='Số lượng học sinh đạt Giỏi', readonly=True, compute='_compute_student_count')
    transcript_ids = fields.One2many('class.transcript', 'class_student_id', string='Bảng điểm')

    @api.depends('transcript_ids')
    def _compute_student_count(self):
        for record in self:
            record.student_count = len(record.transcript_ids)
            record.avg_student_count = len(record.transcript_ids.filtered(lambda r: r.evaluate == 'Tb'))
            record.good_student_count = len(record.transcript_ids.filtered(lambda r: r.evaluate == 'K'))
            record.excellent_student_count = len(record.transcript_ids.filtered(lambda r: r.evaluate == 'G'))
            


class ClassTranscript(models.Model):
    _name = 'class.transcript'
    _description = 'Bảng điểm học sinh'

    class_student_id = fields.Many2one('class.student', string='Lớp học', required=True, ondelete='cascade')
    name = fields.Char(string='Tên học sinh')
    points = fields.Float(string='Điểm số')
    evaluate = fields.Selection([
        ('Tb', 'Trung bình'),
        ('K', 'Khá'),
        ('G', 'Giỏi'),
    ], string='Đánh giá', compute='_compute_evaluate', store=True)

    @api.depends('points')
    def _compute_evaluate(self):
        for record in self:
            if record.points <= 7:
                record.evaluate = 'Tb'
            elif record.points <= 8:
                record.evaluate = 'K'
            else:
                record.evaluate = 'G'
