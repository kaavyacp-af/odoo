from odoo import fields, models, api

class TourismPackage(models.Model):
    _name = "tourism.package"
    _description = "Tourism Package Template"
    _order = "id desc"

    name = fields.Char(string="Package Name", required=True)
    description = fields.Text(string="Overview")
    active = fields.Boolean(string="Active", default=True)
    
    # Pricing & Duration Setup
    base_price = fields.Float(string="Base Price (AED)", required=True, default=100.0)
    duration_days = fields.Integer(string="Duration (Days)", default=1, required=True)
    
    # Custom Relational Categories
    package_type_id = fields.Many2one("tourism.package.type", string="Package Type")
    tag_ids = fields.Many2many("tourism.package.tag", string="Marketing Badges")
    
    # Hotel & Dining Matrix Configurations 
    hotel_star_rating = fields.Selection([
        ('3', '3-Star Budget Properties'),
        ('4', '4-Star Premium Selections'),
        ('5', '5-Star Luxury Resorts')
    ], string="Hotel Tier", default='4', required=True)
    
    boarding_type = fields.Selection([
        ('half', 'Half-Board (Breakfast + Dinner)'),
        ('full', 'Full-Board (All 3 Meals Included)')
    ], string="Boarding Criteria", default='half', required=True)
    
    # Sequential Day Itinerary Multi-line Mapping
    itinerary_day_ids = fields.One2many(
        "tourism.package.day", 
        "package_id", 
        string="Day-by-Day Progression Timeline"
    )

    # Basic UI visual field for the frontend cards framework
    image_1920 = fields.Binary(string="Package Cover Image Attachment")


class TourismPackageDay(models.Model):
    _name = "tourism.package.day"
    _description = "Tourism Package Day Schedule"
    _order = "day_number"

    package_id = fields.Many2one("tourism.package", string="Parent Package Link", ondelete="cascade")
    day_number = fields.Integer(string="Day Number", default=1, required=True)
    title = fields.Char(string="Daily Milestone Title", required=True, placeholder="e.g., Desert Safari & BBQ Dinner")
    narrative = fields.Text(string="Activity Details & Scheduling Directions")
    is_veg_friendly = fields.Boolean(string="Vegetarian Culinary Flag", default=False)