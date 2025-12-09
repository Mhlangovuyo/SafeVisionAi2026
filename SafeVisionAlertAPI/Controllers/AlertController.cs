using Microsoft.AspNetCore.Mvc;

namespace SafeVisionAlertAPI.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class AlertController : ControllerBase
    {
        [HttpPost]
        public IActionResult ReceiveAlert([FromBody] AlertMessage msg)
        {
            Console.WriteLine($"🔥 ALERT RECEIVED: {msg.Alert}");

            return Ok(new { status = "Alert Received" });
        }
    }

    public class AlertMessage
    {
        public string Alert { get; set; }
    }
}
