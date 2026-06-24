from odoo import fields, models, api

class TourismPackage(models.Model):
    _name = "tourism.package"
    _description = "Tourism Package Template"
    _order = "id desc"

    name = fields.Char(string="Package Name", required=True, translate=True)
    description = fields.Text(string="Overview")
    active = fields.Boolean(string="Active", default=True)
    
    base_price = fields.Float(string="Base Price (AED)", required=True, default=100.0)
    duration_days = fields.Integer(string="Duration (Days)", default=1, required=True)
    
    package_type_id = fields.Many2one("tourism.package.type", string="Package Type", ondelete='set null')
    tag_ids = fields.Many2many("tourism.package.tag", string="Marketing Badges")
    
    hotel_star_rating = fields.Selection([
        ('3', '3-Star Budget Properties'),
        ('4', '4-Star Premium Selections'),
        ('5', '5-Star Luxury Resorts')
    ], string="Hotel Tier", default='4', required=True)
    
    boarding_type = fields.Selection([
        ('half', 'Half-Board (Breakfast + Dinner)'),
        ('full', 'Full-Board (All 3 Meals Included)')
    ], string="Boarding Criteria", default='half', required=True)
    
    # Odoo 19 Tip: Use 'inverse_name' consistently and add index=True for performance
    itinerary_day_ids = fields.One2many(
        "tourism.package.day", 
        "package_id", 
        string="Day-by-Day Progression Timeline"
    )

    image_1920 = fields.Image(string="Package Cover Image", max_width=1920, max_height=1920)

class TourismPackageDay(models.Model):
    _name = "tourism.package.day"
    _description = "Tourism Package Day Schedule"
    _order = "day_number, id" # Ordering by day_number is key for progression

    # Odoo 19 Tip: Always index your Many2one fields for faster SQL joins
    package_id = fields.Many2one(
        "tourism.package", 
        string="Parent Package Link", 
        ondelete="cascade", 
        index=True, 
        required=True
    )
    day_number = fields.Integer(string="Day Number", default=1, required=True)
    title = fields.Char(string="Daily Milestone Title", required=True)
    narrative = fields.Text(string="Activity Details")
    is_veg_friendly = fields.Boolean(string="Vegetarian Friendly", default=False)